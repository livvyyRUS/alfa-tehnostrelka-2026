/**
 * Форматирование курсов, результатов и сумм
 * Реализует ФТ-05, ФТ-08, ФТ-14
 * @module core/formatter
 */

/**
 * Форматирует курс с точностью до 4 знаков после запятой
 * @param {number} rate - Курс для форматирования
 * @returns {string} Отформатированный курс
 */
export function formatRate(rate) {
  if (rate === null || rate === undefined || isNaN(rate)) {
    return 'N/A';
  }
  return rate.toFixed(4);
}

/**
 * Форматирует результат конвертации с точностью до 2 знаков после запятой
 * @param {number} result - Результат конвертации
 * @returns {string} Отформатированный результат
 */
export function formatResult(result) {
  if (result === null || result === undefined || isNaN(result)) {
    return 'N/A';
  }
  return result.toFixed(2);
}

/**
 * Форматирует строку курса с указанием валют: "1 USD = 92,5000 RUB"
 * @param {number} rate - Курс
 * @param {string} from - Исходная валюта
 * @param {string} to - Целевая валюта
 * @returns {string} Отформатированная строка
 */
export function formatRateWithCurrency(rate, from, to) {
  const formattedRate = formatRate(rate);
  return `1 ${from} = ${formattedRate} ${to}`;
}

/**
 * Форматирует число с разделителями Thousands
 * @param {number} num - Число для форматирования
 * @returns {string} Отформатированное число
 */
export function formatAmount(num) {
  if (num === null || num === undefined || isNaN(num)) {
    return '0';
  }
  return num.toLocaleString('ru-RU', {
    minimumFractionDigits: 0,
    maximumFractionDigits: 2
  });
}
