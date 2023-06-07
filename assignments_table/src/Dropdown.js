import Pagination from "./Pagination.js";

class Dropdown {
  constructor(datas, options) {
    this.datas = datas;
    this.options = options;
    this.changeEvent = this.changeEvent.bind(this);
    this.render();
  }

  setDropdown() {
    const dropdownArea = document.createElement('select');
    dropdownArea.classList = ['dropdown'];
    
    this.options.forEach(option => {
      const optionTag = document.createElement('option');
      optionTag.value = option;
      optionTag.label = `${option}개씩`;
      dropdownArea.appendChild(optionTag);
    })
    
    dropdownArea.addEventListener('change', this.changeEvent)

    return dropdownArea;
  }

  changeEvent(event) {
    const per = Number(event.target.value);
    const paginationArea = document.getElementsByClassName('paginationArea')[0];
    paginationArea.remove();
    new Pagination(this.datas, 1, per);
  }

  render() {
    const app = document.getElementById('app');

    const dropdownArea = this.setDropdown();
    app.appendChild(dropdownArea);
  }
}

export default Dropdown;