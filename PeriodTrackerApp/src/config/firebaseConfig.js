import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  // paste your config values here
  apiKey: "AIzaSyA-QFMgfRUvfr2VNcpdV-vU9HgT3op9yo0",
  authDomain: "perriodtracker.firebaseapp.com",
  projectId: "perriodtracker",
  storageBucket: "perriodtracker.firebasestorage.app",
  messagingSenderId: "650376923775",
  appId: "1:650376923775:web:75d642c3bff7cfe4fc0d4a"
};

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);