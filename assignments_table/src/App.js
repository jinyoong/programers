import Table from "./Table.js";
import Pagination from "./Pagination.js";
import Dropdown from "./Dropdown.js";

class App {
  constructor($app) {
    this.$app = $app;
    this.render();
  };

  async render() {
    try {
      const response = await fetch("./src/data.json");
      
      if (response.ok) {
        const tableData = await response.json();
        const options = [4, 8];
        console.log("불러온 데이터 : ", tableData);
        new Table(tableData, 0, 4);
        new Pagination(tableData, 1, 4);
        new Dropdown(tableData, options);
      };
    } catch (error) {
      console.log(error)
    }
  };
};

export default App;