function draw_timeline() {
    $('#content').append("<div id='timeline-div' style = 'height:400px'></div>");
    var container = document.getElementById('timeline-div');

    var chart = new google.visualization.Timeline(container);
    var dataTable = new google.visualization.DataTable();

    if (person_selected !== undefined && person_selected!=="") {
        dataTable.addColumn({ type: 'string', id: 'Referente' });
        dataTable.addColumn({ type: 'string', id: 'Processo,Compito' });
    } else {
        dataTable.addColumn({ type: 'string', id: 'Processo' });
        dataTable.addColumn({ type: 'string', id: 'Referente,Compito' });
    }

    dataTable.addColumn({ type: 'date', id: 'Inizio' });
    dataTable.addColumn({ type: 'date', id: 'Fine' });

    timeline = [];
    $(Object.keys(timeline_data)).each( function(index) {
        current_process = timeline_data[index];
        if (person_selected !== undefined && person_selected!=="") {
            row = [current_process.referente,
                current_process.processo + ": "+current_process.compito,
                new Date(current_process.data_inizio.substring(0,4),current_process.data_inizio.substring(5,7)-1,current_process.data_inizio.substring(8,10)),
                new Date(current_process.data_fine.substring(0,4),current_process.data_fine.substring(5,7)-1,current_process.data_fine.substring(8,10))];
        } else {
            row = [current_process.processo,
                current_process.referente + ": "+current_process.compito,
                new Date(current_process.data_inizio.substring(0,4),current_process.data_inizio.substring(5,7)-1,current_process.data_inizio.substring(8,10)),
                new Date(current_process.data_fine.substring(0,4),current_process.data_fine.substring(5,7)-1,current_process.data_fine.substring(8,10))];
            }

        timeline.push(row);
    });

    console.log(timeline);
    dataTable.addRows(timeline);
    chart.draw(dataTable);
}
