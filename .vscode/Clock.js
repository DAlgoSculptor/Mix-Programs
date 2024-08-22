window.addEventListener("DOMContentLoaded",() => {
	const c = new Clock3(".clock");
});

class Clock3 {
	timeUpdateLoop = null;

	constructor(el) {
		this.el = document.querySelector(el);

		this.init();
	}
	init() {
		this.timeUpdate();
	}
	get timeAsObject() {
		const date = new Date();
		let h = date.getHours();
		const m = date.getMinutes();
		const s = date.getSeconds();
		const ap = h > 11 ? "PM" : "AM";
		// milliseconds since 1/1/1970
		const since1970 = date.getTime() - date.getTimezoneOffset() * 60 * 1000;
		// deal with midnight and 13:00
		if (h === 0) h += 12;
		else if (h > 12) h -= 12;

		return { h, m, s, ap, since1970 };
	}
	get timeAsString() {
		let { h, m, s, ap } = this.timeAsObject;
		// prepend 0 to the minute and second if single digits
		if (m < 10) m = `0${m}`;
		if (s < 10) s = `0${s}`;

		return `${h}:${m}:${s} ${ap}`;
	}
	timeUpdate() {
		// update the `aria-label`
		this.el?.setAttribute("aria-label", this.timeAsString);
		// rotate the hands
		const time = this.timeAsObject;
		Object.keys(time).forEach(hand => {
			const handEl = this.el?.querySelector(`[data-hand="${hand}"]`);

			if (handEl) {
				let angle;
				const roundDownSec = Math.floor(time.since1970 / 1000) * 1000;

				if (hand == "h") {
					const msIn12Hrs = 60 * 60 * 12 * 1000;
					angle = roundDownSec % msIn12Hrs / msIn12Hrs;
				} else {
					const msIn1Hr = 60 * 60 * 1000;
					angle = roundDownSec % msIn1Hr / msIn1Hr;
				}

				angle *= 360;
				handEl.style.transform = `rotate(${angle}deg)`;
			}
		});
		// loop
		clearTimeout(this.timeUpdateLoop);
		this.timeUpdateLoop = setTimeout(this.timeUpdate.bind(this),1e3);
	}
}