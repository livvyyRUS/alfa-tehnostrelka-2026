/**
 * Валидация ввода суммы для конвертации
 * Реализует ФТ-06
 * @module core/validator
 */

/**
 * Проверяет, является ли строка корректным числом
 * @param {string} value - Введённое значение
 * @returns {boolean} true если значение является числом
 */
export function isValidNumber(value) {
  if (value === '' || value === null || value === undefined) {
    return true; // пустое значение пропускаем
  }

  // Разрешаем только цифры, точку, запятую, знак минус в начале
  const numericRegex = /^-?\d*\.?\d*$/;
  return numericRegex.test(value);
}

/**
 * Валидирует поле ввода суммы
 * @param {string} value - Введённое значение суммы
 * @returns {Object} Объект { valid: boolean, error: string|null, value: number|null }
 */
export function validateInput(value) {
  // Пустое значение — валидно, считаем как 0
  if (value === '' || value === null || value === undefined) {
    return { valid: true, error: null, value: 0 };
  }

  // Проверяем, является ли строка числом
  if (!isValidNumber(value)) {
    return { valid: false, error: 'Введите корректное число', value: null };
  }

  const numValue = parseFloat(value.replace(',', '.'));

  if (isNaN(numValue)) {
    return { valid: false, error: 'Введите корректное число', value: null };
  }

  // Проверяем на отрицательное число
  if (numValue < 0) {
    return { valid: false, error: 'Сумма должна быть больше нуля', value: null };
  }

  return { valid: true, error: null, value: numValue };
}

/**
 * Валидирует итоговую сумму после парсинга
 * @param {number} amount - Числовое значение суммы
 * @returns {Object} Объект { valid: boolean, error: string|null }
 */
export function validateAmount(amount) {
  if (amount === null || amount === undefined || amount === '') {
    return { valid: true, error: null };
  }

  if (typeof amount === 'string') {
    const parsed = parseFloat(amount.replace(',', '.'));
    if (isNaN(parsed)) {
      return { valid: false, error: 'Введите корректное число' };
    }
    if (parsed < 0) {
      return { valid: false, error: 'Сумма должна быть больше нуля' };
    }
    return { valid: true, error: null };
  }

  if (typeof amount === 'number') {
    if (isNaN(amount)) {
      return { valid: false, error: 'Введите корректное число' };
    }
    if (amount < 0) {
      return { valid: false, error: 'Сумма должна быть больше нуля' };
    }
    return { valid: true, error: null };
  }

  return { valid: false, error: 'Введите корректное число' };
}
