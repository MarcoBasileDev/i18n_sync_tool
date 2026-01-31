const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');

// Handle area click
dropZone.addEventListener('click', () => fileInput.click());

// Tracking handling
['dragover', 'dragleave', 'drop'].forEach(evt => {
    dropZone.addEventListener(evt, e => {
        e.preventDefault();
        e.stopPropagation();
    });
});

dropZone.addEventListener('dragover', () => dropZone.classList.add('drag-over'));
dropZone.addEventListener('dragleave', () => dropZone.classList.remove('drag-over'));

dropZone.addEventListener('drop', e => {
    dropZone.classList.remove('drag-over');
    handleFiles(e.dataTransfer.files);
});

fileInput.addEventListener('change', e => handleFiles(e.target.files));

async function handleFiles(files) {
    for (const file of files) {
        const reader = new FileReader();
        reader.onload = async (e) => {
            const content = e.target.result;
            const success = await eel.upload_file(file.name, content)();
            if (success) {
                console.log(`${file.name} uploaded`);
                refreshFiles();
            }
        };
        reader.readAsText(file);
    }
}

async function refreshFiles() {
    const files = await eel.get_files()();
    const select = document.getElementById('fileSelect');
    select.innerHTML = '';

    if (files.length === 0) {
        select.innerHTML = '<option>No files in /input</option>';
        return;
    }

    files.forEach(f => {
        const opt = document.createElement('option');
        opt.value = f;
        opt.innerText = f;
        select.appendChild(opt);
    });
}

async function startSync() {
    const source = document.getElementById('fileSelect').value;
    if(!source) return alert("Select a source file");

    document.getElementById('syncBtn').innerText = "Processing...";
    const results = await eel.run_sync(source)();

    const resArea = document.getElementById('results');
    resArea.innerHTML = '<h3>Results:</h3>';

    results.forEach(r => {
        resArea.innerHTML += `<div class="result-item"><strong>${r.file}</strong>: ${r.status}</div>`;
    });

    document.getElementById('syncBtn').innerText = "Generate Missing Keys";
    document.getElementById('folderBtn').style.display = "inline-block";
}

function openFolder() {
    eel.open_output_folder()();
}

// Load files on start
refreshFiles();