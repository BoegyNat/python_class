fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => response.json())
  .then((data) => {
    console.log("Title:", data.title);
  })
  .catch((error) => {
    console.error("Error:", error);
  });

const name = "Boegy";
console.log("My name is", name);
console.warn("Warning!");
console.error("Error occurred!");

function calculate(x, y) {
  const result = x + y;
  debugger; // หยุดที่บรรทัดนี้
  return result;
}
calculate(10, 5);
