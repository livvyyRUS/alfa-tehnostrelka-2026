/**
 * Централизованное хранилище состояния приложения
 * Реализует ФТ-02
 * @module state/store
 */

import { loadFromCache, isCacheEmpty } from '../storage/cache.js';

/**
 * Создаёт новое хранилище состояния
 * @returns {Object} Объект хранилища с методами доступа и изменения
 */
export function createStore() {
  const state = {
    baseCurrency: 'USD',
    targetCurrency: 'RUB',
    amount: 0,
    rates: null,
    isCached: false,
    cacheDate: null,
    apiError: null
  };

  // Загружаем кэш при инициализации
  if (!isCacheEmpty()) {
    const cached = loadFromCache();
    if (cached) {
      state.rates = cached.rates;
      state.isCached = true;
      state.cacheDate = cached.timestamp;
      // Определяем базовую валюту из кэша
      if (cached.base && cached.rates[cached.base]) {
        state.baseCurrency = cached.base;
      }
    }
  }

  // Подписчики на изменения
  const subscribers = [];

  /**
   * Подписывается на изменения состояния
   * @param {Function} callback - Функция обратного вызова, вызываемая при изменении
   * @returns {Function} Функция отписки
   */
  function subscribe(callback) {
    subscribers.push(callback);
    return function unsubscribe() {
      const index = subscribers.indexOf(callback);
      if (index > -1) {
        subscribers.splice(index, 1);
      }
    };
  }

  /**
   * Уведомляет всех подписчиков об изменении состояния
   * @param {string} change - Описание изменения
   */
  function notify(change) {
    subscribers.forEach(callback => {
      try {
        callback({ ...state }, change);
      } catch (error) {
        console.error('Ошибка в подписчике:', error);
      }
    });
  }

  /**
   * Возвращает текущую базовую валюту
   * @param {string} currency - Валюта (например, 'USD')
   */
  function setBaseCurrency(currency) {
    if (currency && typeof currency === 'string') {
      state.baseCurrency = currency.toUpperCase();
      notify('baseCurrency');
    }
  }

  /**
   * Возвращает целевую валюту
   * @returns {string} Целевая валюта
   */
  function getBaseCurrency() {
    return state.baseCurrency;
  }

  /**
   * Устанавливает целевую валюту
   * @param {string} currency - Валюта (например, 'RUB')
   */
  function setTargetCurrency(currency) {
    if (currency && typeof currency === 'string') {
      state.targetCurrency = currency.toUpperCase();
      // Проверяем, не совпадают ли валюты
      if (state.baseCurrency === state.targetCurrency) {
        notify('sameCurrency');
      }
      notify('targetCurrency');
    }
  }

  /**
   * Возвращает целевую валюту
   * @returns {string} Целевая валюта
   */
  function getTargetCurrency() {
    return state.targetCurrency;
  }

  /**
   * Устанавливает сумму для конвертации
   * @param {string|number} amount - Сумма
   */
  function setAmount(amount) {
    const numAmount = parseFloat(amount);
    state.amount = isNaN(numAmount) ? 0 : numAmount;
    notify('amount');
  }

  /**
   * Возвращает текущую сумму
   * @returns {number} Сумма
   */
  function getAmount() {
    return state.amount;
  }

  /**
   * Устанавливает курсы валют
   * @param {Object} newRates - Объект с курсами { [currency]: number }
   * @param {string} newBase - Базовая валюта
   */
  function setRates(newRates, newBase = 'USD') {
    if (newRates && typeof newRates === 'object') {
      state.rates = newRates;
      state.baseCurrency = newBase;
      state.isCached = false;
      state.cacheDate = null;
      state.apiError = null;
      notify('rates');
    }
  }

  /**
   * Возвращает курсы валют
   * @returns {Object|null} Объект с курсами или null
   */
  function getRates() {
    return state.rates;
  }

  /**
   * Возвращает флаг использования кэша
   * @returns {boolean} true если используется кэш
   */
  function isCached() {
    return state.isCached;
  }

  /**
   * Устанавливает флаг использования кэша
   * @param {boolean} cached - Флаг кэширования
   */
  function updateCachedFlag(cached) {
    state.isCached = cached;
    if (cached) {
      const cache = loadFromCache();
      if (cache) {
        state.cacheDate = cache.timestamp;
        state.rates = cache.rates;
        state.baseCurrency = cache.base;
      }
    }
    notify('cacheStatus');
  }

  /**
   * Возвращает дату кэширования
   * @returns {number|null} Метка времени или null
   */
  function getCacheDate() {
    return state.cacheDate;
  }

  /**
   * Устанавливает ошибку API
   * @param {string|null} error - Сообщение об ошибке или null
   */
  function setApiError(error) {
    state.apiError = error;
    notify('apiError');
  }

  /**
   * Возвращает текущее состояние
   * @returns {Object} Текущее состояние
   */
  function getState() {
    return { ...state };
  }

  return {
    subscribe,
    setBaseCurrency,
    getBaseCurrency,
    setTargetCurrency,
    getTargetCurrency,
    setAmount,
    getAmount,
    setRates,
    getRates,
    isCached,
    updateCachedFlag,
    getCacheDate,
    setApiError,
    getState
  };
}
