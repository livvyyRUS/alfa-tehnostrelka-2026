/**
 * Клиент для взаимодействия с внешним API курсов валют
 * Реализует ФТ-03
 * @module api/client
 */

import { ApiTimeoutError, ApiHttpError, ApiError, createApiError } from './errors.js';

/**
 * Базовый URL API для получения курсов валют
 */
export const BASE_URL = 'https://api.exchangerate-api.com/v4/latest/USD';

/**
 * Время ожидания ответа от API в миллисекундах
 */
const TIMEOUT_MS = 5000;

/**
 * Отправляет GET-запрос к внешнему API и возвращает парсинг JSON-ответа
 * @param {string} baseUrl - Базовый URL API (по умолчанию BASE_URL)
 * @returns {Promise<Object>} Объект с курсами валют { rates: { [currency]: number } }
 * @throws {ApiTimeoutError} при превышении таймаута
 * @throws {ApiHttpError} при HTTP-ошибке
 * @throws {ApiError} при неизвестной ошибке
 */
export async function fetchRates(baseUrl = BASE_URL) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), TIMEOUT_MS);

  try {
    const response = await fetch(baseUrl, {
      method: 'GET',
      headers: {
        'Accept': 'application/json'
      },
      signal: controller.signal
    });

    clearTimeout(timeoutId);

    if (!response.ok) {
      throw new ApiHttpError(`HTTP-ошибка: ${response.status}`, response.status);
    }

    const data = await response.json();

    if (!data || !data.rates) {
      throw new ApiError('Неверный формат ответа от API');
    }

    return {
      base: data.base || 'USD',
      rates: data.rates
    };

  } catch (error) {
    clearTimeout(timeoutId);
    throw createApiError(error);
  }
}
