import { Injectable } from '@angular/core';

import { catchError, Observable, of, tap } from 'rxjs';

import { Hero } from './heroes/hero';
import { HEROES } from './heroes/mock.heroes';
import { MessageService } from './message.service';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})

export class HeroService {
  constructor(private messageService: MessageService,private httpClient:HttpClient) { }
getHero(id:number):Observable <Hero> {/*id den getiriyor  bunu router için kullancağız*/ 
  const hero=this.httpClient.get<Hero>('http://127.0.0.1:5000/detail/'+id.toString());
  this.messageService.add('HeroService: fetched heroes the Hero with id of  '+id.toString());
  return hero;

}
  
  getHeroes(): Observable<Hero[]> {

   const heroes=this.httpClient.get<Hero[]>('http://127.0.0.1:5000/heroes');
    this.messageService.add('HeroService: fetched heroes');
    return heroes;
  }
  updateHero(hero:Hero):Observable <Hero> {
    return this.httpClient.post<Hero>('http://127.0.0.1:5000/update',hero)
  }
  addHero(hero:Hero):Observable <Hero> {
    
    return this.httpClient.post<Hero>('http://127.0.0.1:5000/add',hero)
  }
  deleteHero(id:number):Observable <Hero> {
    const url = `http://127.0.0.1:5000/delete/${id}`;
    return this.httpClient.delete<Hero>(url);
  }
  searchHeroes(term:string): Observable<Hero[]> {
    if (!term.trim()) {
      // if not search term, return empty hero array.
      return of([]);
    }
    const url = `http://127.0.0.1:5000/search/${term}`;
     
    return this.httpClient.get<Hero[]>(url).pipe(
      tap(heroes => heroes.length ?
         this.log(`Found heroes matching "${term}"`) :
         this.log(`No heroes matching "${term}"`)),
      catchError(this.handleError<Hero[]>('searchHeroes', []))
    );
   }
   private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {
      console.error(`${operation} failed: ${error.message}`);
      return of(result as T);
    }
  }
  private log(message: string): void {
    console.log(`HeroService: ${message}`);
  }
} 