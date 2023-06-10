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
    const maxPageCount = Math.ceil(this.datas.length / per); 
    const paginationArea = document.getElementById('paginationArea');
    paginationArea.innerHTML = '';
    new Pagination(this.datas, maxPageCount, per, 1);
  }

  render() {
    const dropdown = this.setDropdown();
    document.getElementById('dropdownArea').appendChild(dropdown);
  }
}

export default Dropdown;