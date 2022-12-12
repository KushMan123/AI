const MainContainer = (props) => {
	return (
		<section class='main'>
			<div class={`main-top ${props.secondClass}`}>
				<h1>{props.text}</h1>
			</div>
			{props.children}
		</section>
	);
};

export default MainContainer;
