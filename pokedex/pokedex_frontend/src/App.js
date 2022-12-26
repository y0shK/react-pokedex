import logo from './logo.svg';
import './App.css';

async function GetPokemonInfo() {
    const url = 'http://localhost:8000/pokedex_app/pkmn_info'
    try {
      const response = await fetch(url);
      const data = await response.json();
      console.log(data['moves']);

      var data_moves = data['moves']

      var arrayLength = data_moves.length;
      var moves = []

    // https://stackoverflow.com/questions/3010840/loop-through-an-array-in-javascript
    for (var i = 0; i < arrayLength; i++) {
      console.log(data_moves[i]['move']['name'])

      // https://stackoverflow.com/questions/351409/how-to-append-something-to-an-array
      moves.push(data_moves[i]['move']['name'])
    }

    console.log(moves)

    return moves

   

      // Do some stuff with data dict
  } catch (error) {
      console.error(error);
  }

  
}
// console.log(GetPokemonInfo())

// https://stackoverflow.com/questions/32157286/rendering-react-components-from-array-of-objects/64827479#64827479
// {GetPokemonInfo().map(move => <div key={move}> {move} </div>)}
// GetPokemonInfo().then(function(result) {
  // result.map(move => <div key={move}> {move} </div>)
// });
// { moves.map(move => <div key={move}> {move} </div>) }

// https://stackoverflow.com/questions/29516390/how-can-i-access-the-value-of-a-promise

function App() {

  GetPokemonInfo().then(function(response) {

    var moves = response;
    console.log(moves)
    

    

  });
  
  

  return (
    <div className="App">
        
    </div>
  );  

}

export default App;
