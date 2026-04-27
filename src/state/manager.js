/**
 * Менеджер состояния приложения — управляет подписками и изменениями
 * Реализует ФТ-02
 * @module state/manager
 */

import { createStore } from './store.js';

// Глобальный экземпляр хранилища
let storeInstance = null;

/**
 * Инициализирует хранилище состояния (singleton)
 * @returns {Object} Экземпляр хранилища
 */
export function initStore() {
  if (!storeInstance) {
    storeInstance = createStore();
  }
  return storeInstance;
}

/**
 * Возвращает экземпляр хранилища
 * @returns {Object} Экземпляр хранилища
 */
function getStore() {
  if (!storeInstance) {
    return initStore();
  }
  return storeInstance;
}

/**
 * Подписывается на изменения состояния
 * @param {Function} callback - Функция обратного вызова
 * @returns {Function} Функция отписки
 */
export function subscribe(callback) {
  return getStore().subscribe(callback);
}

/**
 * Устанавливает базовую валюту
 * @param {string} currency - ISO-код валюты
 */
export function setBaseCurrency(currency) {
  getStore().setBaseCurrency(currency);
}

/**
 * Устанавливает целевую валюту
 * @param {string} currency - ISO-код валюты
 */
export function setTargetCurrency(currency) {
  getStore().setTargetCurrency(currency);
}

/**
 * Устанавливает сумму для конвертации
 * @param {number|string} amount - Сумма
 */
export function setAmount(amount) {
  getStore().setAmount(amount);
}

/**
 * Устанавливает курсы валют и снимает флаг кэширования
 * @param {Object} rates - Объект с курсами
 * @param {string} base - Базовая валюта
 */
export function setRates(rates, base) {
  getStore().setRates(rates, base);
}

/**
 * Обновляет флаг кэширования
 * @param {boolean} isCached - true если используется кэш
 */
export function updateCachedFlag(isCached) {
  getStore().updateCachedFlag(isCached);
}

/**
 * Устанавливает ошибку API
 * @param {string|null} error - Сообщение об ошибке
 */
export function setApiError(error) {
  getStore().setApiError(error);
}

/**
 * Возвращает текущее состояние
 * @returns {Object} Текущее состояние
 */
export function getState() {
  return getStore().getState();
}
