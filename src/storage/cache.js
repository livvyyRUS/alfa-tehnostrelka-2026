/**
 * Хранилище и кэширование курсов валют в localStorage
 * Реализует ФТ-04, ФТ-13, ФТ-15
 * @module storage/cache
 */

import { CACHES_KEY, TIMESTAMP_KEY, CACHE_TTL } from './keys.js';

/**
 * Сохраняет курсы валют и метку времени в localStorage
 * @param {Object} rates - Объект с курсами валют { [currency]: number }
 * @param {string} base - Базовая валюта (например, 'USD')
 * @returns {boolean} true если сохранение успешно
 */
export function saveToCache(rates, base = 'USD') {
  try {
    const cacheData = {
      rates: rates,
      base: base,
      timestamp: Date.now()
    };

    localStorage.setItem(CACHES_KEY, JSON.stringify(cacheData));
    localStorage.setItem(TIMESTAMP_KEY, String(cacheData.timestamp));

    return true;
  } catch (error) {
    console.error('Ошибка сохранения в кэш:', error);
    return false;
  }
}

/**
 * Загружает курсы валют из localStorage
 * @returns {Object|null} Объект с курсами { rates, base, timestamp } или null если кэш пуст
 */
export function loadFromCache() {
  try {
    const ratesData = localStorage.getItem(CACHES_KEY);
    const timestampData = localStorage.getItem(TIMESTAMP_KEY);

    if (!ratesData || !timestampData) {
      return null;
    }

    const parsed = JSON.parse(ratesData);
    const timestamp = parseInt(timestampData, 10);

    if (isNaN(timestamp)) {
      clearCache();
      return null;
    }

    // Проверяем актуальность кэша (TTL)
    if (Date.now() - timestamp > CACHE_TTL) {
      return null;
    }

    return {
      rates: parsed.rates || {},
      base: parsed.base || 'USD',
      timestamp: timestamp
    };

  } catch (error) {
    console.error('Ошибка загрузки из кэша:', error);
    clearCache();
    return null;
  }
}

/**
 * Очищает кэш в localStorage
 * @returns {boolean} true если очистка успешна
 */
export function clearCache() {
  try {
    localStorage.removeItem(CACHES_KEY);
    localStorage.removeItem(TIMESTAMP_KEY);
    return true;
  } catch (error) {
    console.error('Ошибка очистки кэша:', error);
    return false;
  }
}

/**
 * Проверяет, пустой ли кэш
 * @returns {boolean} true если кэш пуст
 */
export function isCacheEmpty() {
  try {
    return !localStorage.getItem(CACHES_KEY);
  } catch (error) {
    console.error('Ошибка проверки кэша:', error);
    return true;
  }
}
