import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  user: null,
  points: 0,
  isAuthenticated: false,
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    login: (state, action) => {
      state.user = action.payload;
      state.isAuthenticated = true;
    },
    logout: (state) => {
      state.user = null;
      state.isAuthenticated = false;
      state.points = 0;
    },
    updatePoints: (state, action) => {
      state.points = action.payload;
    },
  },
});

export const { login, logout, updatePoints } = userSlice.actions;
export default userSlice.reducer;
