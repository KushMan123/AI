import React, { useEffect, useRef } from "react";

const Card = (props) => {
	const num = useRef();

	useEffect(() => {
		if (num !== null) {
			let interval = 3000;
			let startValue = 0;
			let endValue = parseInt(num.current.getAttribute("data-val"));
			let duration = Math.floor(interval / endValue);
			let counter = setInterval(() => {
				startValue += 1;
				num.current.textContent = startValue;
				if (startValue == endValue) {
					clearInterval(counter);
				}
			}, duration);
		}
	}, [num]);

	return (
		<div class='card'>
			{props.children}
			<span class='num' data-val={`${props.dataValue}`} ref={num}>
				000
			</span>
			<span class='text'>{props.text}</span>
		</div>
	);
};

export default Card;
