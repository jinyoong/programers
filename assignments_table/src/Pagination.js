class Pagination {
  constructor(currentPage, per) {
    this.currentPage = currentPage;
    this.per = per;
    this.render();
  }

  makePagination(app) {
    const paginationArea = document.createElement('div');
    paginationArea.className = 'paginationArea';

    for (let i = 0; i <= this.per + 1; i++) {
      const page = document.createElement('button');
      page.classList = ['page']
      let content;
      
      if (i === 0) {
        content = '<<';
      } else if (i === this.per + 1) {
        content = '>>';
      } else {
        content = `${i}`;
      }

      page.textContent = content;
      page.addEventListener('click', this.clickEvent.bind(this));
      // bind로 넘기지 않으면, clickEvent 내부에서 this는 엘리먼트를 참조한다.
      // 그래서 this가 참조할 대상을 bind로 넘겨줘야 한다.

      paginationArea.appendChild(page);
    }

    app.appendChild(paginationArea);
  }

  setPageStyle() {
    const page = document.getElementsByClassName('page');

    for (let i = 1; i <= this.per; i++) {
      
      if (this.currentPage === i) {
        page[i].classList.add('active');
      } else {
        page[i].classList = ['page'];
      }
    }
  }

  clickEvent(event) {
    const clickPage = Number(event.target.innerText);
    this.currentPage = clickPage;
    this.setPageStyle()
  }

  render() {
    const app = document.getElementById('app');
    this.makePagination(app);
    this.setPageStyle();
  }
}

export default Pagination;