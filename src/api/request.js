/**
 * Обёртка для запросов к API с таймаутом и повторными попытками
 * Реализует ФТ-03, ФТ-12
 * @module api/request
 */

import { ApiTimeoutError, ApiHttpError, ApiError } from './errors.js';
import { fetchRates } from './client.js';

/**
 * Отправляет запрос к API с таймаутом в 5 секунд и одной повторной попыткой
 * @param {string} baseUrl - Базовый URL API (по умолчанию BASE_URL из client.js)
 * @returns {Promise<Object>} Объект с курсами валют { rates, base }
 * @throws {ApiTimeoutError} при превышении таймаута
 * @throws {ApiHttpError} при HTTP-ошибке
 * @throws {ApiError} при неизвестной ошибке
 */
export async function fetchWithTimeout(baseUrl) {
  return fetchRates(baseUrl);
}

/**
 * Отправляет запрос к API с таймаутом и повторной попыткой (до 2 попыток)
 * @param {string} baseUrl - Базовый URL API
 * @param {number} retries - Количество попыток (по умолчанию 2)
 * @param {number} retryDelay - Задержка между попытками в мс (по умолчанию 1000)
 * @returns {Promise<Object>} Объект с курсами валют { rates, base }
 * @throws {ApiTimeoutError} при превышении таймаута всех попыток
 * @throws {ApiHttpError} при HTTP-ошибке всех попыток
 * @throws {ApiError} при неизвестной ошибке всех попыток
 */
export async function fetchWithRetry(baseUrl, retries = 2, retryDelay = 1000) {
  let lastError = null;

  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const result = await fetchWithTimeout(baseUrl);
      return result;
    } catch (error) {
      lastError = error;

      if (attempt < retries) {
        // Небольшая задержка перед повторной попыткой
        await new Promise(resolve => setTimeout(resolve, retryDelay));
      }
    }
  }

  // Все попытки исчерпаны — выбрасываем последнюю ошибку
  throw lastError;
}
