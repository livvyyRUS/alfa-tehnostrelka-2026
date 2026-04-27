/**
 * Ключи для хранения в localStorage
 * Реализует ФТ-04, ФТ-13
 * @module storage/keys
 */

/**
 * Ключ для хранения курса валют
 */
export const CACHES_KEY = 'currency_rates_cache';

/**
 * Ключ для хранения метки времени кэша
 */
export const TIMESTAMP_KEY = 'currency_rates_timestamp';

/**
 * Время жизни кэша в миллисекундах (24 часа)
 */
export const CACHE_TTL = 24 * 60 * 60 * 1000;
