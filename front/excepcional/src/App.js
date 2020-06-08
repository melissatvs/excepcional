import React from 'react'
import Header from "./components/header"
import { Provider } from 'react-redux'
import store from '../src/redux/reducer'
import Routes from "./routes"
import Footer from './components/footer'
import './styles/reset.css'
import './styles/index.css'
import './styles/forms.css'

function App() {
  return (
    <Provider store={store}>
      <Header />
      <Routes />
      <Footer />
    </Provider>
  );
}

export default App;
