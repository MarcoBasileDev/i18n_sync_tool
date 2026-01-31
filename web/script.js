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