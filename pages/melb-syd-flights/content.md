Many Australians say that our country is too large and too low-density to justify high speed rail.
However, no one is proposing high speed rail from Broome to Bourke.
The Melbourne-Sydney flight corridor is one of the busiest in the world, with [4 million](https://www.bitre.gov.au/sites/default/files/documents/domestic-aviation-activity-2024.pdf) round trips each year, or 22,000 one way trips per day, over a distance that is shorter than Paris to Berlin.

In this post I visualise the extremely high number of planes leaving on a typical day, and estimate the total amount of emissions from those planes, including a monetary estimate of those emissions.
Planes emit CO<sub>2</sub>, but also several other harmful gases, such as nitrous oxides (NO<sub>x</sub>), sulfur oxides (SO<sub>x</sub>), unburnt fuel (hydrocarbons, HC) and particulate matter (PM), which I include.

## Results

<a href="animation.mp4">
   <video autoplay loop class="video appear"  width=100% autobuffer muted playsinline video-auto-ctrl  preload defaultMuted>
      <source src="animation.mp4" type="video/mp4">
      <source src="animation.webm" type="video/webm">
   </video>
</a>


| Gas | Quantity | Cost (AUD) |
|-----|----------|-----------|
| CO<sub>2</sub> | 4,535 tonnes | 2,701,282 |
| NO<sub>x</sub> | 27.5 tonnes | 900,039 |
| SO<sub>x</sub> | 1.2 tonnes | 60,409 |
| PM | 198 kg | 6,499 |
| CO | 4.6 tonnes | 5,196 |
| HC | 559 kg | 3,658 |
| **Total** | | **$ 3,677,082** |



The total pollution damage in a typical day is **$2.7 million** (AUD).
To put this in perspective, the [operating profit (EBITA)](https://aviationweek.com/air-transport/airports-networks/australias-major-airports-see-surge-aeronautical-revenue) of Sydney airport is about $1.56 million per day, across all flights (not just from Melbourne).

High speed rail would last several decades. Over a 30 year time span, the emissions of this flight corridor would amount to $30 billion emissions damage.
If high speed rail was built, there would still be some planes, so this estimate must be adjusted down. (However with the construction of a second Sydney airport, total traffic may increase.)
[Cost estimates](https://en.wikipedia.org/wiki/High-speed_rail_in_Australia) for such a line vary from $50 to $200 billion (or 1-6 AUKUS submarines).
It is not the purpose of this post to weight up the overall costs and benefits of high speed rail in Australia.
Rather, the purpose is to focus on one of the benefits, and make a clear visualisation of how extreme the status quo is.

## Assumed Shadow Prices of Emissions

| Pollutant | Damage Cost |
|---|---|
| Carbon Dioxide (CO<sub>2</sub>) | 595.65 AUD/tonne |
| Carbon Monoxide (CO) | 1.1317 AUD/kg |
| Nitrogen Oxides (NOx) | 32.75 AUD/kg |
| Sulfur Oxides (SOx) | 49.95 AUD/kg |
| Particulate Matter (PM) | 32.75 AUD/kg |
| Hydrocarbons (HC) | 6.5404 AUD/kg |

The damage estimate for each gas is proportional to this choice of shadow price.
In theory, this should equal the marginal damage of emissions. However, these are hard numbers to estimate, particularly for CO<sub>2</sub>.
Estimates in the academic literature of the marginal damage of CO<sub>2</sub> vary between 80 USD/tonne to 1500 USD/tonne (and even higher).
I personally lean towards the higher end of academic estimates. This number came from [Rennert et al. 2022](https://www.nature.com/articles/s41586-022-05224-9) (308 USD/tonne if you choose a 1.5% discount rate).
Many people may challenge this choice, arguing for a lower number, based on the market price of carbon today.

Government prices and market prices based on government-created markets (e.g. EU-ETS and ACCUs) are far lower than marginal damage and the expected price of carbon, because they are set by [unambitious politicians](https://theshovel.com.au/2021/10/26/man-announces-he-will-quit-drinking-by-2050/). (Sometimes politicians set the quantity, not the price, but a low quantity results in a low price.) Consider the incentives of a politician with a 3-6 year election cycle. Will they overestimate or underestimate the importance of long term climate damage? (More technically, is their pure rate of time preference higher than what you think an ethically defensible rate is?) Admittedly, academics estimating marginal damage have poor incentives too (you won't get tenure if your calculations yield an estimate with a different number of zeros to your peers), but still, I trust the academics more.
To summarise the difference, low carbon prices today reflect the low cost reducing emissions, and high estimates of the shadow price of carbon reflect the high benefit of reducing emissions. The only way there could be no gap is if governments are doing enough to combat climate change, proportional to the harms it will bring. I think that is simply not true.

However, since those government numbers drive government investment decisions, I also did analysis with that.
The AEMC uses a price of [80 AUD/tonne in 2026](https://www.aemc.gov.au/sites/default/files/2024-03/AEMC%20guide%20on%20how%20energy%20objectives%20shape%20our%20decisions%20clean%20200324.pdf) (Table A.1, page 19).
With this price, CO<sub>2</sub> damage is $365,801 per day, bringing the total to $1.33 million.
Interestingly, with this lower shadow price of carbon, the biggest pollutant by far (by dollar cost) is nitrous oxide cost, at triple the cost of carbon damage. I found this surprising, however there is [research](https://www.sciencedaily.com/releases/2019/11/191107202553.htm) showing that this is indeed the case.

For other pollutants:

- Carbon monoxide is 1.9 times worse than CO<sub>2</sub>, according to [this IPCC estimate](https://archive.ipcc.ch/publications_and_data/ar4/wg1/en/ch2s2-10-3-2.html).
- For sulfur oxides, nitrous oxides and particulate matter, the [Victorian Environmental Protection Agency](https://www.nepc.gov.au/sites/default/files/2022-09/aaq-nepm-impact-statement-appendix-c.pdf) uses numbers from the [UK government](https://www.gov.uk/government/publications/assess-the-impact-of-air-quality/air-quality-appraisal-damage-cost-guidance). For nitrous oxides and particulate matter, there are aircraft specific numbers.
- For hydrocarbons (HC), there are local harms from inhaling carcinogens, and there are indirect climate effects. For the local harms, I use a price of £150/tonne from [the UK government](https://www.gov.uk/government/publications/assess-the-impact-of-air-quality/air-quality-appraisal-damage-cost-guidance). For the climate damage, I use a multiplier from CO<sub>2</sub> damage of 10.5, from [Fry et al. (2014)](https://acp.copernicus.org/articles/14/523/2014/acp-14-523-2014.pdf).


## Methodology

I have published my code for this on [GitHub](https://github.com/mdavis-xyz/melb-syd-flight-emissions). You can check my assumptions, reproduce the results, or modify the methodology. Reproducing the results for another set of airports should be quite straightforward.

## Data

I took historical flight data from the [OpenSky Network](https://openskynetwork.github.io/opensky-api/rest.html). (Their underlying dataset is free, useful and impressive. However their API and [Python client library](https://openskynetwork.github.io/opensky-api/index.html) is quite buggy and difficult to use, so I made [my own fork](https://github.com/mdavis-xyz/opensky-api/tree/fork).) For each model of aircraft, I obtained the emissions intensity from [the European Environment Agency](https://www.eea.europa.eu/publications/emep-eea-guidebook-2023/part-b-sectoral-guidance-chapters/1-energy/1-a-combustion/1-a-3-a-aviation.3/view) via [The Wayback Machine](https://web.archive.org/web/20260000000000*/https://www.eea.europa.eu/publications/emep-eea-guidebook-2023/part-b-sectoral-guidance-chapters/1-energy/1-a-combustion/1-a-3-a-aviation.3/at_download/file).

The data does not contain the exact flight paths, only the start and end points.
I animated them linearly, at constant speed, plus some random [jitter](https://r4ds.hadley.nz/layers.html#:~:text=jitter) to spread the planes out. (Otherwise they would be on top of each other.)

The passenger count per plane is a simple estimate based on an annual figure of [8.04 million](https://www.bitre.gov.au/sites/default/files/documents/domestic-aviation-activity-2024.pdf) passengers per year (one way), assuming an equal number of flights per day, and equal number of passengers per flight. This is of course not accurate, but passenger count is not the focus of this project, emissions are.

### Scope

I looked at flights travelling between Sydney, both Melbourne airports, and Canberra, because those could all be reduced with a Sydney to Melbourne high speed train.
I excluded the emissions from travel to and from the airport. The pollution from taxis by business travellers from Melbourne airport to the city centre is probably substantial compared to the flight's emissions (I guess ~10%), however high speed rail passengers may also catch taxis to and from the station, depending on whether it is built in the city centre or outside the city.

These emissions intensities are not just for carbon dioxide (CO<sub>2</sub>), but also carbon monoxide (CO), nitrous oxides (NO<sub>x</sub>), sulfur oxides (SO<sub>x</sub>), hydrocarbons (unburnt fuel) and particulate matter (PM).

If you want to know per passenger emissions, perhaps to inform your own travel choices, I recommend [Google Flights](https://www.google.com/travel/flights/). However for this analysis I want per plane emissions. (The number of passengers or seats per plane varies, and is hard to estimate.)

## Conclusion

Australia's large size and low population density is not a valid argument against high speed rail between three of our large, close capital cities.
The damage that this flight corridor is imposing upon others is comparable to the producer surplus of these companies that do not pay for their negative externalities. This probably does not make the business case for high speed rail add up on its own, but it helps substantially.

There are many reasons to be skeptical of high speed rail proposals in Australia. A lack of faith in the ability of the federal or state government (of any party) to deliver the project is justifiable. (When is the last time a large nation-building infrastructure project was built on time, and within budget?) Australia's eminent domain powers (think [_The Castle_](https://www.imdb.com/title/tt0118826/)) are possibly too weak, and Qantas has [an unreasonably strong influence over federal politicians](https://www.goodreads.com/book/show/223545245-the-chairman-s-lounge). Qantas would not let high speed rail happen.

This article is not intended to be a definitive argument about the overall decision to build high speed rail in Australia (even though I think we should). Rather, it is a first pass at quantifying an important piece of the puzzle.
