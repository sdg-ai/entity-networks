from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel
from entity_extraction import EntityExtractor

#TODO: Add validations and error cases

class InputText(BaseModel):
    text: str

class InputTrends(BaseModel):
    trends: list = []

x = EntityExtractor()
app = FastAPI()

@app.get("/entities-example")
def extract_entities_example():

    example_string_2 = "By Scott Simone, Contributor On May 2, Chris Ballinger stood on stage of the Future Blockchain Summit in Dubai and made a striking announcement: " \
                        "He’d formed a global consortium of automakers to create an ecosystem that would allow blockchain technology to thrive in the transportation industry." \
                        "The nonprofit organization, mobility open blockchain initiative (mobi), consists of auto giants such as BMW, General Motors, Ford, and Renault, along with " \
                        "companies in the tech, financial, and insurance industries.  It’s all about building trust in a business network between otherwise untrusting parties, "\
                        "Ballinger said.Industry executives have expressed excitement at the prospect of the new technology. "\
                        "We believe blockchain will transform the way people and businesses interact, creating new opportunities in mobility,  Rich Strader, "\
                        "vice president of mobility product solutions at Ford, explained.The announcement, which has been a year in the making, comes on the heels " \
                        "of at least half a dozen auto industry titans announcing forays into the world of blockchain technology. And while most of these projects are in their infancy, "\
                        "Ballinger and his coalition are operating around one ideal: If applied correctly, blockchain can revolutionize the auto industry, "\
                        "and it’s very likely that the industry will look tremendously different a decade from today.Ballinger started toying with blockchain technology when he was head of innovation "\
                        "and new mobility at the Toyota Research Institute.He began seeing movement toward on-demand mobility whereby the infrastructure was pay-per-use, "\
                        "rather than outright purchasing new cars.  I began thinking that in that world, blockchain [and] distributed ledger was the perfect fit because these cars’ "\
                        "infrastructures need to communicate,  Ballinger explained.  They need ways of making machine payments, paying for use, paying for congestion, paying for tolls, " \
                        "paying for energy as they go, and having secure identities for both the car and the riders. Under his tutelage, the Toyota Research Institute presented proofs of "\
                        "concept that utilized blockchain technology to address these concerns. Yet while they were successful in theory, the idea failed to take off. "\
                        "I began noticing that that wasn’t unusual at all,  Ballinger said.  I kept seeing big companies stick an asset on the blockchain, make a public announcement, " \
                        "then have it go nowhere. The reason, according to Ballinger, is that there was no ecosystem that would help those ideas thrive.  If there’s nothing else in the network, "\
                        "the technology alone is useless, Ballinger said.  It’s like email or fax back in the day; if there’s no one to send an email to, or a fax to, your fax machine is just a good doorstop. "\
                        "And so building the ecosystem was the quickest step that was needed. According to Ballinger,  Blockchain and related trust-enhancing technologies are poised to redefine the automotive "\
                        "industry and how consumers purchase, insure, and use vehicles. By bringing together automakers, suppliers, startups, and government agencies, we can accelerate "\
                        "adoption for the benefit of businesses, consumers, and communities.Blockchain and related trust-enhancing technologies are poised to redefine the automotive industry and how "\
                        "consumers purchase, insure, and use vehicles. By bringing together automakers, suppliers, startups, and government agencies, we can accelerate adoption for the benefit of businesses, "\
                        "consumers, and communities. Chris Ballinger, CEO and Founder at MOBI: Mobility Open Blockchain InitiativeIn the first few months of 2018, it seemed like there was a new "\
                        "announcement every day about an auto giant dabbling with blockchain technology.In late March, for example, Ford received a patent to use cryptocurrency and blockchain technology "\
                        "so that cars could communicate with—and, at times, pay—each other while on the road. The revolutionary idea was laid out in the patent application as follows:This system "\
                        "would temporarily allow for … vehicles to drive at higher speeds in less-occupied lanes of traffic and also to merge and pass freely when needed. Other … vehicles voluntarily " \
                        "occupy slower lanes of traffic to facilitate the consumer vehicle to merge into their lanes and pass as needed.But the patent, according to Karen Hampton, a spokesperson " \
                        "for Ford Motor Company, isn’t necessarily indicative of a current product plan. Rather, it represents the company’s willingness to explore new ideas.  "\
                        "Patent applications are intended to protect new ideas, but they aren’t necessarily an indication of new business or product plans,  said Hampton.A few days later, " \
                        "Audi announced that it, too, was testing blockchain technology for its physical and financial distribution processes, aiming to increase security and transparency in its global " \
                        "supply chains. Porsche is exploring the utilization of blockchain apps in its vehicles in cooperation with the Berlin-based startup XAIN. And BMW is reportedly planning " \
                        "to expand its portfolio by partnering with UK startup Circulor to eliminate battery minerals produced by child labor.Perhaps furthest along in developing an automotive-based use " \
                        "for blockchain is Mercedes Benz, which is currently testing its app MobiCoin to reward drivers for environmentally-cautious driving. MobiCoin uses blockchain technology to pair " \
                        "a smartphone app to technology already available in Mercedes Benz vehicles that measures how  green  the car is driving. Depending on how green the driver operates a vehicle, drivers "\
                        "will earn  coins  through the app that can be redeemed for rewards, such as VIP tickets for high-profile events like the MercedesCup final. MobiCoin " \
                        "technology is an experiment to find out how technology can influence behavior,  Jonas von Malottki, senior manager finance and controlling solutions at Daimler, " \
                        "which owns Mercedes, said.  The idea was that we wanted to create something that is car-centric and incentivizes green driving. And while von Malottki had a lot of people "\
                        "explaining to him the different ways the company should use blockchain, it became clear they weren’t the right forms.  For [MobiCoin], we have a coin behind it, " \
                        "so it was good to use blockchain,  he explained.  It’s the type of technology that allows us to make it very people-centric—blockchain makes it a lot easier and a lot more trustworthy. "\
                        "Like the other companies, Mercedes is just in the testing phase; after the two-month test is complete, it will evaluate whether or not it will make MobiCoin available worldwide. " \
                        "Experts Say: They’ll Be Sorry Auto industry insiders and blockchain technology experts agree that if automakers don’t innovate and make use of blockchain now, well, they’ll be sorry. " \
                        "The times are changing to more autonomous, self-driving, electric [cars],  von Malottki described.  We’re adapting to this generation, and we have to change our business model more " \
                        "and more to do so. I think blockchain is one of the technologies that is very much augmented for this type of change. According to Teodoro Lio, managing director and industrial and " \
                        "automotive innovation lead at Accenture, blockchain will drastically affect the auto industry—from the handling of vehicle ID numbers and collision histories to the complex supply chains " \
                        "that lead to assembly lines and dealerships.  Industry leaders are just beginning to understand the unique characteristics of this technology and its diverse forms,  he said. "\
                        "For Derin Cag, founder of Richtopia and co-founder of Marketing Runners and Blockchain Age, companies are jumping onto the blockchain bandwagon both because of the tremendous opportunity " \
                        "and also what will happen if they don’t. If they don’t do it, the competition is going to, and destroy a big segment of their business,  Cag articulated.  The group that does it right the "\
                        "first time is really going to transform the industry as it exists today. In five to 10 years, the industry will not be the same, because of all the transformations. "

    annotations = x.get_annotations(example_string_2)

    '''
	for i, annotation in enumerate(annotations):
		print('============== {} =============='.format(i))
		print(annotation[0],'\n',annotation[1],'\n entityType:',annotation[2]['entityType'], '\n wiki_classes:',annotation[2]['wiki_classes'],'\n url:',annotation[2]['url'], '\n dbPediaIri:',annotation[2]['dbPediaIri'])


		print('\n')

	return annotations
    '''
    return {"entity-networks": annotations}


@app.post("/entities")
def extract_entities(input_text: InputText):
    annotations = x.get_annotations(input_text.text)
    return annotations

@app.post("/batch-entities")
def batch_extract_entities(trend_results: InputTrends):
    for item in trend_results.trends:
        item['extract_entities'] = x.get_annotations(item['text'])

    return {"entity-networks-trends": trend_results}
