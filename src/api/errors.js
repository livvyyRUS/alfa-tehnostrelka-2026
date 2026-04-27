/**
 * Исключения модуля API
 * Реализует ФТ-03, ФТ-12
 * @module api/errors
 */

/**
 * Базовая ошибка API
 */
export class ApiError extends Error {
  /**
   * @param {string} message - Сообщение об ошибке
   * @param {string} code - Код ошибки
   */
  constructor(message, code = 'API_ERROR') {
    super(message);
    this.name = 'ApiError';
    this.code = code;
  }
}

/**
 * Ошибка таймаута API
 */
export class ApiTimeoutError extends ApiError {
  /**
   * @param {string} message - Сообщение об ошибке
   */
  constructor(message = 'Превышено время ожидания ответа от API') {
    super(message, 'API_TIMEOUT');
    this.name = 'ApiTimeoutError';
  }
}

/**
 * Ошибка HTTP-ответа API
 */
export class ApiHttpError extends ApiError {
  /**
   * @param {string} message - Сообщение об ошибке
   * @param {number} status - Код HTTP-статуса
   */
  constructor(message = 'Ошибка HTTP-ответа от API', status = 0) {
    super(message, 'API_HTTP_ERROR');
    this.name = 'ApiHttpError';
    this.status = status;
  }
}

/**
 * Создаёт экземпляр ошибки API из объекта Response или ошибки AbortController
 * @param {Response|Error} error - Объект Response или ошибка
 * @returns {ApiError}
 */
export function createApiError(error) {
  if (error instanceof ApiError) {
    return error;
  }

  if (error instanceof TypeError && error.message && error.message.includes('abort')) {
    return new ApiTimeoutError();
  }

  if (error instanceof TypeError && error.message && error.message.includes('network')) {
    return new ApiError('Ошибка сети. Проверьте подключение к интернету', 'NETWORK_ERROR');
  }

  return new ApiError('Неизвестная ошибка API');
}
