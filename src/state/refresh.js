/**
 * Фоновое обновление кэша курсов валют
 * Реализует ФТ-16
 * @module state/refresh
 */

import { isCached, getBaseCurrency } from './store.js';
import { saveToCache } from '../storage/cache.js';
import { fetchWithTimeout } from '../api/request.js';
import { setRates, updateCachedFlag, setApiError, subscribe } from './manager.js';

/**
 * Интервал фоновой проверки в миллисекундах (30 секунд)
 */
const REFRESH_INTERVAL = 30000;

let refreshTimer = null;

/**
 * Запускает фоновое обновление кэша каждые 30 секунд
 * @param {Object} store - Экземпляр хранилища состояния
 * @param {Function} onRefreshSuccess - Callback при успешном обновлении
 * @param {Function} onRefreshError - Callback при ошибке обновления
 */
export function startBackgroundRefresh(store, onRefreshSuccess, onRefreshError) {
  if (refreshTimer) {
    stopBackgroundRefresh();
  }

  refreshTimer = setInterval(async () => {
    try {
      await checkAndRefresh(store, onRefreshSuccess, onRefreshError);
    } catch (error) {
      if (onRefreshError) {
        onRefreshError(error);
      }
    }
  }, REFRESH_INTERVAL);
}

/**
 * Останавливает фоновое обновление кэша
 */
export function stopBackgroundRefresh() {
  if (refreshTimer) {
    clearInterval(refreshTimer);
    refreshTimer = null;
  }
}

/**
 * Проверяет и обновляет кэш при восстановлении API
 * @param {Object} store - Экземпляр хранилища состояния
 * @param {Function} [onRefreshSuccess] - Callback при успешном обновлении
 * @param {Function} [onRefreshError] - Callback при ошибке обновления
 */
export async function checkAndRefresh(store, onRefreshSuccess, onRefreshError) {
  // Проверяем, нужно ли обновлять (только если используется кэш)
  if (!isCached()) {
    return;
  }

  try {
    const baseCurrency = getBaseCurrency();
    const baseUrl = `https://api.exchangerate-api.com/v4/latest/${baseCurrency}`;

    const data = await fetchWithTimeout(baseUrl);

    // Успешное обновление
    if (store) {
      store.setRates(data.rates, data.base);
      updateCachedFlag(false);
      saveToCache(data.rates, data.base);
      setApiError(null);
    }

    if (onRefreshSuccess) {
      onRefreshSuccess(data);
    }

    // Останавливаем фоновое обновление при успешном обновлении
    stopBackgroundRefresh();

  } catch (error) {
    // API по-прежнему недоступен — просто игнорируем
    if (onRefreshError) {
      onRefreshError(error);
    }
  }
}
