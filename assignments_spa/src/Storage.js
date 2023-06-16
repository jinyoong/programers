async function setPersonalInfo() {
  const response = await fetch("src/data/new_data.json");
  const data = await response.json();
  
  console.log(data);
}

export default setPersonalInfo;