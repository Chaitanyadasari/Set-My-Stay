import React, { Component } from 'react';
import axios from 'axios';
import List from '@material-ui/core/List'
class Home extends Component {

	constructor(props) {
		super(props);
		this.state = {
            userid: '', 
            solotrip: '', 
            holiday: '', 
            smalltrip: '',
            city: '',
            listings: [],
			status: null
        };
      
}


 useridChangeHandler = e => {
 this.setState({
   userid: e.target.value
 });
};

solotripChangeHandler = e => {
 this.setState({
   solotrip: e.target.value
 });
};

holidayChangeHandler = e => {
 this.setState({
   holiday: e.target.value
 });
};

smalltripChangeHandler = e => {
    this.setState({
      smalltrip: e.target.value
    });
   };

cityChangeHandler = e => {
    this.setState({
      city: e.target.value
    });
   };
   
submitHandler = e => {
    e.preventDefault();

		 axios.get('http://localhost:5000/ensemble/' + this.state.userid + '/'  + this.state.solotrip + '/' + this.state.holiday + '/' + this.state.smalltrip  + '/' + this.state.city)
            .then(response => {
                       {
                          console.log(response)
                        this.setState({listings: this.state.listings.concat(response.data.data)});              
                      }
                    })
                    .catch(err => {
                        console.log(err);
                      });
                    };
		




	render(){
   
   
    const con =  this.state.listings.map((item, i) => {
            return(
               <div>
                  <p> Recommended Listing </p>
                  <div>
                         {item} </div>
    </div>
                
            )
        })

		return (
         
			<div className="container">
				<h1 className="display-4">Set My Stay Dashboard</h1>
				<form>
					<div className="form-group">
						<label for="userid">User Id</label>
						<input type="text" className="form-control" value={this.state.userid} onChange={this.useridChangeHandler} id="userid" required/>
					</div>
                   
                    <div className="form-group">
						<label for="solotrip">Is it a Solo Trip if yes Enter 1</label>
						<input type="text" className="form-control" value={this.state.solotrip} onChange={this.solotripChangeHandler} id="solotrip" required />
					</div>
                    <div className="form-group">
						<label for="holiday">Is it a Holiday Trip if yes Enter 1</label>
						<input type="text" className="form-control" value={this.state.holiday} onChange={this.holidayChangeHandler} id="holiday" required />
					</div>
                    <div className="form-group">
						<label for="smalltrip">Is it a Short Trip if yes Enter 1</label>
						<input type="text" className="form-control" value={this.state.smalltrip} onChange={this.smalltripChangeHandler} id="smalltrip" required />
					</div>
                    <div className="form-group">
						<label for="city">Please Enter the  city are you visiting</label>
						<input type="text" className="form-control" value={this.state.city} onChange={this.cityChangeHandler} id="city" required />
					</div>
					<button type="button" onClick={this.submitHandler}  className="btn btn-primary">Get Recommnedation</button>
					<small class="form-text text-muted">Complete the form to enable this button.</small>
				</form>
				
				<footer class="footer mt-auto py-3">
					<div class="container">
                    <span class="text-muted">Sai Chaitanya Dasari , Kedar Acharya , Parshwa Gandhi </span>

						<span class="text-muted">By Set My Trip for CMPE 256  </span>
                       
						<a href="https://github.com/Chaitanyadasari/Set-My-Stay">Github Link</a>
					</div>
				</footer>
                <div>
                   
                <List >
                <h2>Get Top 10 Recommendation stay places for you </h2>
                             {con}
                             </List>
                             
            </div>

			</div>
            
		);
	}
}


export default Home;