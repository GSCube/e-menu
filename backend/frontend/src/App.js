import React, {Component} from 'react';
import ReactTable from 'react-table';
import axios from 'axios';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      details: false,
      detailsPerson: [],
      personName:[],
      persons: []
    };
    this.showDetails = this.showDetails.bind(this);
    this.hideDetails = this.hideDetails.bind(this);
  }
  componentDidMount() {
    axios.get(`https://jsonplaceholder.typicode.com/users`).then(res => {
      const persons = res.data;
      this.setState({persons});
    })
  }
  showDetails(personId, personName) {
    let person = this.state.persons.find(person => person.id === personId);
    let detailsPerson = [person.address];
    this.setState({
      personName,
      detailsPerson,
      details: true,
    });
  }

  hideDetails() {
      this.setState({
        details: false
    });
  }

  render() {
    const mainColumns = [
      {
        Header: 'Id',
        accessor: 'id',
        Cell: (props) => {
            return(
                <div className="back" onClick={() => this.showDetails(props.original.id, props.original.name)}>
                    {props.value}
                </div>
            )
        }
      }, {
        Header: 'Name',
        accessor: 'name',
        Cell: (props) => {
            return(
                <div className="back" onClick={() => this.showDetails(props.original.id, props.original.name)}>
                    {props.value}
                </div>
            )
        }
      }, {
        Header: 'Username',
        accessor: 'username',
        Cell: (props) => {
            return(
                <div className="back" onClick={() => this.showDetails(props.original.id, props.original.name)}>
                    {props.value}
                </div>
            )
        }
      }
    ]

    const detailsColumns = [
      {
        Header: 'City',
        accessor: 'city',
      }, {
        Header: 'Street',
        accessor: 'street'
      }, {
        Header: 'Zip code',
        accessor: 'zipcode'
      }, {
        Header: 'Suite',
        accessor: 'suite'
      }
    ]
    return (<div className="App">
      <div className="table-container">
        {
          this.state.details
            ? <div>
                <h1>{this.state.personName}</h1>
                <ReactTable columns={detailsColumns} data={this.state.detailsPerson} defaultPageSize={4} defaultSorted={[{
                      id: "id"
                    }
                  ]}/>
                <h2 className='back' onClick={this.hideDetails}>Go back</h2>
              </div>

            : <div>
                <h1>Menu</h1>
                <ReactTable columns={mainColumns} data={this.state.persons} defaultPageSize={4} defaultSorted={[{
                        id: "id"
                      }
                    ]}/>
              </div>
        }
      </div>
    </div>);
  }
}

export default App;
