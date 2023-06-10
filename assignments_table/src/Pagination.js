class Pagination {
  constructor(datas, maxPageCount, datasOfPage, currentPage) {
    this.datas = datas;
    this.maxPageCount = maxPageCount;
    this.datasOfPage = datasOfPage;
    this.currentPage = currentPage;
    // bind로 넘기지 않으면, clickEvent 내부에서 this는 엘리먼트를 참조한다.
    // 그래서 this가 참조할 대상을 bind로 넘겨줘야 한다.
    // 아니면 화살표 함수를 사용해야 this가 Pagination 클래스를 참조한다.
    this.render();
  }

  pageContent(page) {
    let result;

    if (page === 0) {
      result = '<<';
    } else if (page === this.maxPageCount + 1) {
      result = '>>';
    } else {
      result = String(page);
    }

    return result;
  }

  drawPaginationButtons() {
    const pagination = document.createElement('div');
    pagination.classList = 'pagination';

    for (let page = 0; page <= this.maxPageCount + 1; page++) {
      const button = document.createElement('button');
      button.textContent = this.pageContent(page);

      button.addEventListener('click', (event) => {
        this.clickEvent(event);
      })

      pagination.appendChild(button);
    }

    return pagination;
  }

  drawTableByNewData() {
    const start = (this.currentPage - 1) * this.datasOfPage;
    const end = Math.min(this.datas.length, this.currentPage * this.datasOfPage);
    const tableBody = document.getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';

    for (let i = start; i < end; i++) {
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
  }

  setPaginationButtonsStyle() {
    const buttons = document.getElementsByTagName('button');
    
    for (let page = 1; page <= this.maxPageCount; page++) {
      const button = buttons[page];
      button.classList = ['pagination'];

      if (page === this.currentPage) {
        button.classList.add('active');
      }
    }
  }

  clickEvent(event) {
    const clickedButton = event.target.textContent;
    
    if (clickedButton === '<<') {
      this.currentPage = 1;
    } else if (clickedButton === '>>') {
      this.currentPage = this.maxPageCount;
    } else {
      this.currentPage = Number(clickedButton);
    }

    this.drawTableByNewData()
    this.setPaginationButtonsStyle()
  }

  render() {
    const pagination = this.drawPaginationButtons();
    
    document.getElementById('paginationArea').appendChild(pagination);
    this.drawTableByNewData();
    this.setPaginationButtonsStyle();
  }
}

export default Pagination;