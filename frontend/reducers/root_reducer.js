import { combineReducers } from 'redux';
import ProjectReducer from './project_reducer';

const rootReducer = combineReducers({
  project: ProjectReducer
});

export default rootReducer;
