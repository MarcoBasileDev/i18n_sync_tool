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