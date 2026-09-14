fetch('../JavaScript/data.json')
    .then(response => {
        if (!response.ok) {
            throw new Error(`Could not load data.json: ${response.status}`);
        }
        return response.json();
    })
    .then(students => {
        const tableBody = document.getElementById('table-body');

        tableBody.innerHTML = '';

        students.forEach(student => {
            const row = document.createElement('tr');

            [student.id, student.name, student.age, student.course, student.score]
                .forEach(value => {
                    const cell = document.createElement('td');
                    cell.textContent = value;
                    row.appendChild(cell);
                });

            tableBody.appendChild(row);
        });
    })
    .catch(error => {
        console.error(error);
    });