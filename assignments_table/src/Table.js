class Table {
  constructor(datas) {
    this.datas = datas;
    this.render();
  };

  drawTableHead() {
    const tableHead = document.createElement('thead');
    const tableHeadTr = document.createElement('tr');
    const tableHeadItems = ['이름', '팀', '등번호', '포지션'];
    
    tableHeadItems.forEach(tableHeadItem => {
      const th = document.createElement('th');
      th.textContent = tableHeadItem;

      tableHeadTr.appendChild(th);
    })

    tableHead.appendChild(tableHeadTr);
    return tableHead;
  }

  drawTableBody() {
    const tableBody = document.createElement('tbody');
    
    for (let i = 0; i < this.datas.length; i++) {
      const tableBodyTr = document.createElement('tr');
      const data = this.datas[i];

      tableBodyTr.innerHTML = `
        <td>${data.name}</td>
        <td>${data.team}</td>
        <td>${data.number}</td>
        <td>${data.position}</td>
      `

      tableBody.appendChild(tableBodyTr);
    }

    return tableBody;
  }

  render() {
    const table = document.createElement('table');
    table.classList = ['table'];

    const thead = this.drawTableHead();
    table.appendChild(thead);

    const tbody = this.drawTableBody();
    table.appendChild(tbody);

    document.getElementById('tableArea').appendChild(table);

  };
};

export default Table;