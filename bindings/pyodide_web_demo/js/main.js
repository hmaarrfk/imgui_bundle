// ===========================
// Layouting: tooltips, editor
// ===========================

// Initialize Split.js for resizable panes
Split(['#editor-container', '#canvas-container'], {
    sizes: [25, 75], // Adjusted sizes as per user's update
    minSize: 0,    // Minimum size of each pane in pixels
    gutterSize: 8,
    cursor: 'col-resize',
    onDrag: () => {
        onSplitDrag();
    }
});

function onSplitDrag() {
    // Trigger window resize event, so that Emscripten can adjust its canvas size
    window.dispatchEvent(new Event('resize'));
}

// Initialize CodeMirror for the code editor
const editor = CodeMirror(document.getElementById('editor'), {
    mode: 'python',
    lineNumbers: true,
    theme: 'eclipse', // Optional: Change theme as desired
    value: initial_example_code(),
});

// Adjust CodeMirror size to fill the container
editor.setSize('100%', '100%');

// Initialize Tippy.js tooltips with HTML content
document.addEventListener('DOMContentLoaded', () => {
    tippy('.logo', {
        allowHTML: true, // Allow HTML content in tooltips
        placement: 'bottom',
        animation: 'scale',
        arrow: true,
        delay: [100, 100],
        theme: 'light-border',
        // Optional: You can customize the tooltip further here
    });
});

// =====================================
// Add event listener for the Run button
// =====================================
const runButton = document.getElementById('run-button');
runButton.addEventListener('click', runEditorPythonCode);


// =====================================
// Then, initialize everything
// =====================================
async function initialize() {
    await loadPyodideAndPackages();
    await load_pyodide_imgui_render();
    await passCanvasToPyodide();
}

initialize();
