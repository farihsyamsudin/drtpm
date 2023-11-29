document.addEventListener('DOMContentLoaded', function () {
    // Ambil tombol "Tambah Extra" dengan ID 'addExtraButton'
    var addButton = document.getElementById('addForm');

    addButton.addEventListener('click', function () {
        // Ambil parameter 'extra' dari URL saat ini
        var currentExtra = parseInt(new URL(window.location.href).searchParams.get('extra')) || 0;

        // Tambah 1 ke 'extra'
        var newExtra = currentExtra + 1;

        // Redirect ke URL baru dengan 'extra' yang ditingkatkan
        window.location.href = '/fishtograph/data-tangkapan/tambah/?extra=' + newExtra;
    });

    var minForm = document.getElementById('minForm');

    minForm.addEventListener('click', function () {
        var currentExtra = parseInt(new URL(window.location.href).searchParams.get('extra')) || 0;

        if (currentExtra > 1) {
            var newExtra = currentExtra - 1;

            window.location.href = '/fishtograph/data-tangkapan/tambah/?extra=' + newExtra;
        }
    });
});
