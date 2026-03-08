const vscode = require('vscode');

function isPipeLinePrefix(textBeforeCursor) {
  return /^\s*\|>.*$/.test(textBeforeCursor);
}

async function insertPipeContinuation(editor) {
  const selection = editor.selection;
  const line = editor.document.lineAt(selection.active.line);
  const before = line.text.slice(0, selection.active.character);

  if (!selection.isEmpty || !isPipeLinePrefix(before)) {
    await vscode.commands.executeCommand('default:type', { text: '\n' });
    return;
  }

  const indent = (before.match(/^\s*/) || [''])[0];
  const text = `\n${indent}|> `;
  await editor.edit((editBuilder) => {
    editBuilder.insert(selection.active, text);
  });
}

function activate(context) {
  const disposable = vscode.commands.registerCommand('micelio.enterPipe', async () => {
    const editor = vscode.window.activeTextEditor;
    if (!editor) {
      await vscode.commands.executeCommand('default:type', { text: '\n' });
      return;
    }

    await insertPipeContinuation(editor);
  });

  context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
  activate,
  deactivate,
};
