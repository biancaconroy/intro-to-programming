# intro-to-programming
Project Summary: ClubTime? helps partygoers discover how busy clubs are in real time with a green, yellow, and red system. Users can view maps of a city to find popular clubs, and see how busy the clubs a partygoer would wanting to go to are based on crowd estimates. 

Tech Stack: Google Maps, Redux/API, GeoLocation

List of Functions/modules to build: MapView, CLubCard, CrowdLogic, SearchBar, LocationService, ClubAPI, Favorites

Folder Structure: 
club-crowd-app/
├── /assets/            # Images, icons, etc.
├── /components/        # Reusable components like ClubCard, Indicator
├── /screens/           # Screens: MapScreen, ClubDetail, SearchScreen
├── /services/          # API calls, Location service
├── /context/           # Global state or Redux store
├── /utils/             # Helper functions, crowd color logic
├── /admin-panel/       # Optional web admin portal (separate React app)
├── /backend/           # Express server & Firebase/DB scripts
│   ├── /routes/
│   ├── /controllers/
│   └── /models/
├── App.js              # Main app entry point
├── README.md           # This file
└── package.json


