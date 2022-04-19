// Unique key is setup here
const key = '4fb3598019c9f2b0dc36c6518e6ad958';

const requestByCity = async (city) => {
    const baseURLDaily = 'http://api.openweathermap.org/data/2.5/weather'
    const queryDaily = `?q=${city}&appid=${key}`;

    const baseURLHourly = 'https://api.openweathermap.org/data/2.5/forecast'
    const queryHourly = `?q=${city}&appid=${key}`;


    //make fetch call (promise call)
    const dailydata = await fetch(baseURLDaily + queryDaily);
  

    const hourlydata = await fetch(baseURLHourly + queryHourly);
    
    //promise data
    const daily  = await dailydata.json();
    const hourly = await hourlydata.json();
    const data = [daily,hourly];
    return data;
}

const requestByCoord = async (lat, lon) => {
    
    const baseURLDaily = 'http://api.openweathermap.org/data/2.5/weather'
    const queryDaily = `?lat=${lat}&lon=${lon}&appid=${key}`;

    const baseURLHourly = 'https://api.openweathermap.org/data/2.5/forecast'
    const queryHourly = `?lat=${lat}&lon=${lon}&appid=${key}`;

    //make fetch call (promise call)
    const dailydata = await fetch(baseURLDaily + queryDaily);
    const hourlydata = await fetch(baseURLHourly + queryHourly);


    const daily = await dailydata.json();
    const hourly = await hourlydata.json();
    const data = [daily, hourly];
    return data;
}

