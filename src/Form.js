imports

const formSchema = yup.object().shape({
	username:
	email:
	password:
	confirmPass:
});

export default function signUp() {
	//useStates
	const [buttonDisabled, setButtonDisabled] = useState(true);
	
	const [formState, setFormState] = useState({
		username:
		email:
		password:
		confirmPass:
	});

	const [errors, setErros] = useState({
		username:
		email:
		password:
		confirmPass:
	});

	const [post, setPost] = useState([]);

	//button use
	useEffect(() => {
		formSchema
			setButtonDisabled(!valid);
	}, [formState]);


	//event functions
	const formSubmit = e => {
		axios.post(/*api*/, formState)
		.then(res => {});
		.catch(err =>);
	};

	const validateChange = e => {
		yup.reach(formSchema, /*target*/)
			.validate(/*code*/)
			.then(valid => {
				setErrors({/*code*/})
			})
			.catch(err => {
				setErrors({/*code*/})
			});
	};

	const inputChange = e => {
		e.persist();
		const newFormData = {/*code*/}

		validateChange(e);
		setFormState(newFormData);
	}

	return(
		<form onSubmit = {formSubmit}>
			<label htmlFor = "username">
				Enter username
				<input id = "username"
					type = "text"
					name = "username"
					value = {formState.username}
				/>
				{errors.name.length > 0 ? <p className = "error">{errors.name}</p> : null}//
			</label>/

			<label htmlFor = "email">
				Enter username
				<input id = "email"
					type = "text"
					name = "email"
					value = {formState.email}
				/>
				{errors.name.length > 0 ? <p className = "error">{errors.name}</p> : null}//
			</label>/

			<label htmlFor = "password">
				Enter username
				<input id = "password"
					type = "password"
					name = "password"
					value = {formState.password}
				/>
				{errors.name.length > 0 ? <p className = "error">{errors.name}</p> : null}//
			</label>/

			<label htmlFor = "confirmPass">
				Enter username
				<input id = "confirmPass"
					type = "password"
					name = "confirmPass"
					value = {formState.confirmPass}
				/>
				{errors.name.length > 0 ? <p className = "error">{errors.name}</p> : null}//
			</label>/

		 	<button disabled = {buttonDisabled}>Submit</button>//
		 </form>/


		//Link to sign in page
		 <Link to = "/signInPage">Already a member? Sign in here!</Link>
		);
}







