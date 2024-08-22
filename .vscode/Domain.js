const circles = document.getElementsByClassName("circle");
const circleSeconds = circles[2];
const circleMinutes = circles[1];
const circleHours = circles[0];

const TIME_STAMP_SEC = document.querySelector(".time-stamp.seconds");
const TIME_STAMP_MIN = document.querySelector(".time-stamp.minutes");
const TIME_STAMP_HOUR = document.querySelector(".time-stamp.hours");

const timeContainer = document.querySelector(".time");

[...circles].forEach((circle) => {
  const dot = document.createElement("div");
  dot.classList.add("dot");
  circle.appendChild(dot);
});

let date = new Date();

let ms = date.getMilliseconds();
let sec = date.getSeconds();
let min = date.getMinutes();
let hour = date.getHours();
let am = hour < 12;

setTime(ms, sec, min, hour);
setTimeCircles(ms, sec, min, hour);

const changeTime = setInterval(() => {
  let date = new Date();

  let ms = date.getMilliseconds();
  let sec = date.getSeconds();
  let min = date.getMinutes();
  let hour = date.getHours();
  let am = hour < 12;

  setTime(ms, sec, min, hour, am);
  setTimeCircles(ms, sec, min, hour);
}, 500);

function setTime(ms, s, min, h, am) {
  s = s > 9 ? s : "0" + s;
  min = min > 9 ? min : "0" + min;
  h = h > 12 ? h - 12 : h;
  h = h > 9 ? h : "0" + h;
  const timeCycle = am ? "am" : "pm";

  TIME_STAMP_SEC.textContent = s;
  TIME_STAMP_MIN.textContent = min;
  TIME_STAMP_HOUR.textContent = h;
  timeContainer.dataset.time = timeCycle;
}
function setTimeCircles(ms, s, min, h, am) {
  s = (s / 60) * 100;
  min = (min / 60) * 100;
  h = h > 12 ? h - 12 : h;
  h = (h / 12) * 100;

  circleSeconds.setAttribute("style", `--per: ${s}`);
  circleMinutes.setAttribute("style", `--per: ${min}`);
  circleHours.setAttribute("style", `--per: ${h}`);
}
