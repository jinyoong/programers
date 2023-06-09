class Pagination {
  constructor(datas) {
    this.datas = datas;
    // bind로 넘기지 않으면, clickEvent 내부에서 this는 엘리먼트를 참조한다.
    // 그래서 this가 참조할 대상을 bind로 넘겨줘야 한다.
    this.render();
  }

  pageContent(maxPageCount, page) {
    let result;

    if (page === 0) {
      result = '<<';
    } else if (page === maxPageCount + 1) {
      result = '>>';
    } else {
      result = String(page);
    }

    return result;
  }

  drawPaginationButtons(maxPageCount, datasOfPage, currentPage) {
    const pagination = document.createElement('div');
    pagination.classList = 'pagination';

    for (let page = 0; page <= maxPageCount + 1; page++) {
      const button = document.createElement('button');
      button.textContent = this.pageContent(maxPageCount, page);
      button.classList = ['pageButton'];

      if (page === currentPage) {
        button.classList.add('active');
      }

      pagination.appendChild(button);
    }

    return pagination;
  }

  render() {
    let maxPageCount = 5;
    let datasOfPage = 4;
    let currentPage = 1;
    const pagination = this.drawPaginationButtons(maxPageCount, datasOfPage, currentPage);

    document.getElementById('paginationArea').appendChild(pagination);
  }
}

export default Pagination;