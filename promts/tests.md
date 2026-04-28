You are a QA engineer. Write a Node.js script that tests the application in `output/src/index.html`. The test script will be executed with `node test.js` from the `output/tests` directory.

## Testing approach
Since we have an HTML file, you cannot directly simulate browser events in plain Node. Instead, you must **extract the JavaScript logic** from the HTML and test it as pure functions. To do that, follow this pattern:

1. The HTML file's JavaScript is assumed to define functions that implement the business logic (e.g., `calculate(expr)`, `TaskManager.addTask(title, desc)`). The code generation agent will be instructed to structure code in that way.
2. In the test script, read the HTML file from `../src/index.html`, extract the `<script>` content, and use `eval()` (or a proper sandbox) to define those functions.
3. Then write unit tests with assertions (simple `if`/`throw`). At the end, output "All tests passed" or "Error: ..." with details.

Example test.js skeleton:
```javascript
const fs = require('fs');
const html = fs.readFileSync('../src/index.html', 'utf8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) throw new Error('No script found');
eval(scriptMatch[1]); // defines functions

// Test FR-01: addition
const result = calculate('2+3');
if (result !== 5) throw new Error('Expected 5, got ' + result);
console.log('Test FR-01 passed');
// ... more tests
console.log('All tests passed');