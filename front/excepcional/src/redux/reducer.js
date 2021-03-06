import { createStore } from 'redux';

const initialState = {
   user: {},
   erros: []
};

const store = createStore(
   reducer, 
   window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
   );
   
function reducer(state = initialState, action) {
   
   switch (action.type) {
      case 'GET_USER':
      return {
         ...state,
         user: action.payload
      };

      case 'PUT_USER':
      return {
         ...state,
         user: action.payload
      }; 
      
      case 'GET_ERROS':
      return {
         ...state,
         erros: action.payload
      };

      default:
      return state;
   }
}
   
export default store