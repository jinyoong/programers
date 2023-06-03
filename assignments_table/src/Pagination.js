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
      const page = document.createElement('div');
      page.classList = ['page']

      if (this.currentPage === i) {
        page.classList.add('current');
      }

      let content;

      if (i === 0) {
        content = '<<';
      } else if (i === this.per + 1) {
        content = '>>';
      } else {
        content = `${i}`;
      }

      page.textContent = content;

      paginationArea.appendChild(page);
    }

    app.appendChild(paginationArea);
  }

  clickEvent() {
    
  }

  render() {
    const app = document.getElementById('app');
    this.makePagination(app);
  }
}

export default Pagination;