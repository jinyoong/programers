class Table {
  constructor(data, start, count) {
    this.data = data;
    this.start = start;
    this.count = count;
    this.render();
  };

  makeHead(tableArea) {
    const tableHead = document.createElement('thead');
    tableHead.className = "thead";
  
    const tableHeadLine = document.createElement("tr");
    const tableHeadElements = ["이름", "소속팀", "등번호", "포지션"];
    
    tableHeadElements.forEach(element => {
      const tableHeadElement = document.createElement("th");
      tableHeadElement.textContent = element;
  
      tableHeadLine.appendChild(tableHeadElement);
    });
  
    tableHead.appendChild(tableHeadLine);
    tableArea.appendChild(tableHead);
  };

  makeBody(tableArea) {
    const tableBody = document.createElement("tbody");
    tableBody.className = "tbody";

    for (let i = 0; i < this.count; i++) {
      const idx = this.start + i;
      const tableBodyLine = document.createElement("tr");

      tableBodyLine.innerHTML = `
        <td>${this.data[idx].name}</td>
        <td>${this.data[idx].team}</td>
        <td>${this.data[idx].number}</td>
        <td>${this.data[idx].position}</td>
      `;

      tableBody.appendChild(tableBodyLine);
    };

    tableArea.appendChild(tableBody);
  };

  render() {
    const tableArea = document.getElementById('table');
    tableArea.className = "table";
    
    this.makeHead(tableArea);
    this.makeBody(tableArea);
  };
};

export default Table;