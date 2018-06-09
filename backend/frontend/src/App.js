import React, {Component} from 'react';
import ReactTable from 'react-table';
import axios from 'axios';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      details: false,
      detailsdish: [],
      dishName: [],
      dishes: []
    };
    this.showDetails = this.showDetails.bind(this);
    this.hideDetails = this.hideDetails.bind(this);
  }
  componentDidMount() {
    axios.get(`/api/get_menues_and_dishes`).then(res => {
      const dishes = res.data;
      this.setState({dishes});
    })
  }
  showDetails(dishId, dishName) {
    let dish = this.state.dishes.find(dish => dish.id === dishId);
    let detailsdish = dish.dishes;
    this.setState({
      dishName,
      detailsdish,
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
                <div className="back" onClick={() => this.showDetails(props.original.id, props.original.title)}>
                    {props.value}
                </div>
            )
        }
      }, {
        Header: 'Title',
        accessor: 'title',
        Cell: (props) => {
            return(
                <div className="back" onClick={() => this.showDetails(props.original.id, props.original.title)}>
                    {props.value}
                </div>
            )
        }
      }
    ]

    const detailsColumns = [
      {
        Header: 'Title',
        accessor: 'title',
      }, {
        Header: 'Price',
        accessor: 'price'
      }
    ]
    return (<div className="App">
      <div className="table-container">
        {
          this.state.details
            ? <div>
                <h1>{this.state.dishName}</h1>
                <ReactTable columns={detailsColumns} data={this.state.detailsdish} defaultPageSize={4} defaultSorted={[{
                      id: "id"
                    }
                  ]}/>
                <h2 className='back' onClick={this.hideDetails}>Go back</h2>
              </div>

            : <div>
                <h1>Menu</h1>
                <ReactTable columns={mainColumns} data={this.state.dishes} defaultPageSize={4} defaultSorted={[{
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
