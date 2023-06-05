class Pagination {
  constructor(datas, currentPage, per) {
    this.datas = datas;
    this.currentPage = currentPage;
    this.total = datas.length;
    this.per = per;
    this.clickEvent = this.clickEvent.bind(this);
    // bind로 넘기지 않으면, clickEvent 내부에서 this는 엘리먼트를 참조한다.
    // 그래서 this가 참조할 대상을 bind로 넘겨줘야 한다.
    this.render();
  }

  makePagination(app) {
    const paginationArea = document.createElement('div');
    const maxPage = Math.ceil(this.total / this.per);
    paginationArea.className = 'paginationArea';

    for (let i = 0; i <= maxPage + 1; i++) {
      const page = document.createElement('button');
      page.classList = ['page']
      let content;
      
      if (i === 0) {
        content = '<<';
      } else if (i === maxPage + 1) {
        content = '>>';
      } else {
        content = `${i}`;
      }

      page.textContent = content;
      page.addEventListener('click', this.clickEvent);

      paginationArea.appendChild(page);
    }

    app.appendChild(paginationArea);
  }

  setPageStyle() {
    const page = document.getElementsByClassName('page');
    const maxPage = Math.ceil(this.total / this.per);

    for (let i = 1; i <= maxPage; i++) {
      
      if (this.currentPage === i) {
        page[i].classList.add('active');
      } else {
        page[i].classList = ['page'];
      }
    }
  }

  setTablePage(start, end) {
    const tableBody = document.getElementsByTagName('tbody')[0];
    tableBody.replaceChildren();

    for (let i = start; i < end; i++) {
      const tableBodyLine = document.createElement('tr');

      tableBodyLine.innerHTML = `
        <td>${this.datas[i].name}<td>
        <td>${this.datas[i].team}<td>
        <td>${this.datas[i].number}<td>
        <td>${this.datas[i].position}<td>
      `;

      tableBody.appendChild(tableBodyLine);
    }
  }

  buttonToNumber(clickNumber) {
    let result = 1;

    if (clickNumber === '<<') {
      result = 1;
    } else if (clickNumber === '>>') {
      result = Math.ceil(this.total / this.per);
    } else {
      result = Number(clickNumber);
    }

    return result;
  }

  clickEvent(event) {
    const clickPage = this.buttonToNumber(event.target.innerText);
    const start = this.per * (clickPage - 1);
    const end = this.per * clickPage;
    this.currentPage = clickPage;
    this.setPageStyle()
    this.setTablePage(start, end);
  }

  render() {
    const app = document.getElementById('app');
    this.makePagination(app);
    this.setPageStyle();
  }
}

export default Pagination;