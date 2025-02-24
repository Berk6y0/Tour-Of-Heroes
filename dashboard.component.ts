import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HEROES } from '../heroes/mock.heroes';
import { Hero } from '../heroes/hero';
import { HeroService } from '../hero.service';
import { HeroDetailComponent } from '../hero-detail/hero-detail.component';
import { RouterModule } from '@angular/router';
import { HeroSearchComponent } from '../hero-search/hero-search.component';
@Component({
  selector: 'app-dashboard',
  imports: [CommonModule,RouterModule,HeroSearchComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.css'
})
export class DashboardComponent implements OnInit{
heroes:Hero[]=[];
constructor(private heroService:HeroService){}

ngOnInit():void{
this.getHeroes()
}
  getHeroes() {
    this.heroService.getHeroes().subscribe(x => this.heroes=x.slice(1,5))
  
  }/*Hero service  kullanarak gerekli bilgileri çektik*/

}
