import logo from './logo.svg';
import './App.css';
import Plot from 'react-plotly.js';
import React, {Component} from 'react';

class App extends Component {
  constructor(props) {
    super(props);


    this.state = {
//      images that we fetch from the model
      images: null,
//      flags for html show/hide components
      showImage:false,
      showForm: true,
      showProgress:false,
      showError:false
    };
    this.runKMmean = this.runKMmean.bind(this);
  };

  runKMmean(ev) {
    ev.preventDefault();
    this.setState({showProgress: !this.state.showProgress});
    this.setState({showForm: !this.state.showForm});
    const data = new FormData();
    data.append('k_param', this.clustersNumber.value);
    fetch('/data', {
      method: 'POST',
      body: data,
    }).then((response) => response.json()
    ).then((res)=>
        {
         this.setState({images:res});
         this.setState({showProgress: !this.state.showProgress});
         this.setState({showImage: !this.state.showImage});
        })
         .catch((error) => {
    console.error('Error:', error);
    this.setState({showProgress: !this.state.showProgress});
    this.setState({showError: !this.state.showError});

  });
}

  render() {
  const {showImage,showForm,showProgress, showError, images} = this.state;
    return (
    <body>
    <center>
       {showForm && (
  <form onSubmit={this.runKMmean}>
        <div>
        <h3 text-align= "center">Enter the number of clusters you want</h3>
          <input ref={(ref) => { this.clustersNumber = ref; }} type="text" placeholder="" />
        </div>
        <br/>
        <div>
          <button>submit</button>
        </div>

         </form>)
         }
         {showProgress && (<label>Uploading Document: <progress value="70" max="100">70 %</progress></label>)}
         {showError && "there was a error"}
         {showImage && images.map((image) => (
        <p key={image.name}>
          <h1>Cluster: {image.name}</h1>
          <p><h3>centroid image</h3></p>
          <span><img styles={{minWidth: 500, minHeight: 500}}
           src={`data:image/png;base64,${image.centred}`}/></span>
           <p><h3>random images from the cluster </h3></p>
          <span class="cluster-image"> <img src={`data:image/png;base64,${image.img_from_cluster_0}`}/></span>
          <span class="cluster-image"><img src={`data:image/png;base64,${image.img_from_cluster_1}`}  /></span>
          <span class="cluster-image"><img src={`data:image/png;base64,${image.img_from_cluster_2}`} /></span>
          <span class="cluster-image"><img src={`data:image/png;base64,${image.img_from_cluster_3}`} /></span>
          <span class="cluster-image"><img src={`data:image/png;base64,${image.img_from_cluster_4}`} /></span>
        </p>
      ))}
      </center>
 </body>
    );
  }
}
export default App;


