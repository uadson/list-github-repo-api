function dataRepo(dataRepo) {
    document.getElementById('search').value = '';
    let param = 'dataRepo=' + dataRepo;
    send_request(param);
}

function send_request(param) {
    $.ajax({
        method: 'GET',
        url: 'api/repos?' + param,
        beforeSend: function () {
            console.log('before send');
        },
        success: function (result) {
            update_table(result);
            console.log('after send');
        },
        error: function () {
            console.log('error');
        }
    });
}

function update_table(data) {
    let row;
    let all_rows = '';

    Object.keys(data).forEach(key => {
        elem = data[key];
        row = '<tr><td>' + elem['name'] + '</td>' + '<td>' + elem['url'] + '</td>' + '<td>' + elem['status'] + elem['commits'] + elem['last_commit'] + elem['languagens'] + '</td>' + '</tr>';
        all_rows = all_rows + row;
    });

    $('#myTable tbody').html(all_rows);
}