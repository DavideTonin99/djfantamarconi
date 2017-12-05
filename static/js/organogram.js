function draw_organogram() {
    console.log(organogram_data);
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Nome');
    data.addColumn('string', 'Livello Superiore');
    data.addColumn('string', 'Informazioni');

    var organogram = []

    for (person_id in organogram_data) {
        current_person = organogram_data[person_id];
        row = [
            {v:current_person.name + " " +current_person.surname,f:current_person.name+" "+current_person.surname+"<br><div class='role'>"+current_person.sector.toUpperCase()+": "+current_person.role+"</div>"},
            organogram_data[current_person.parent_level.toString()].name + " " + organogram_data[current_person.parent_level.toString()].surname,
            current_person.email
        ];
        organogram.push(row);
    }

    data.addRows(organogram);

    // Create the chart.
    var chart = new google.visualization.OrgChart($('#content').get(0));
    // Draw the chart, setting the allowHtml option to true for the tooltips.
    chart.draw(data, {allowHtml:true,allowCollapse:true});
}
