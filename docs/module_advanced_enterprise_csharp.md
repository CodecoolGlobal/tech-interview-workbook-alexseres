# Enterprise module (C# branch)

### ASP.NET Core, WCF

#### What Is the difference between .NET Core and .NET Standard? How do them relate to “classic” .NET?
    -NET Core is a free,  cross-platform, open source implementation of the managed framework for Windows, Linux and macOS operating System. It is a cross-platform successor to .NET Framework.It supports types of applications like console, ASP.NET Core, cloud and Universal Windows Platform. 

    -.NET Standard: This is the set of fundamental APIs (commonly referred to as base class library or BCL) that all .NET implementations must implement. By targeting .NET Standard, you can build libraries that you can share across all your .NET apps, no matter on which .NET implementation or OS they run. There are various implementations of .NET. Each implementations allows .Net code to execuite  different places(linux, macOs, Windows etc.).NET Standard is a formal specification of the API's that are common across all these .NET implementations. Net Standard is not a framerowk or platform of its own. It does not have implementations or a runtime, it just defines a specification what different .NET platforms has to implement to remain .NET Standard compilant.
#### What is ASP.NET MVC?
    -ASP.NET MVC is a free web framework for building web applciations on e.g. .NET core using HTML, CSS, And Javascript. 
    -ASP.NET MVC is based on Model-VIew-Controller(MVC) architecture. Developers can build dynamic web applications using ASP.NET MVC framework that enables a clean separation of concerns, fast development.
#### Can you explain Model, Controller and View in MVC?
    -Model: it represents the shape of the data. A class in c# is used to describe a model. Model objects store data retrieved from the database.
    -View in MVC is a user interface. View display model data to the user and also enables them to modify them. VIew in ASP.NET core  is Html, CSS and some special syntax(Razor syntax) that makes it easy to communicate with the model and controller.
    -The controller handles the user request. Typically, the user uses the view and raises an HTTP request, which will be handled by the controller. THe controller processes the request and returns the appropriate view as response
#### Explain the page lifecycle of MVC.
    -1.Routing
        -All the requests are routed to a special class called Controller. The controller is responsible for generating the response and sending the content back to the browser
    -2.Url Routing Module intercepts the request
        -Whenever you make a request against an ASP.NET MVC application, the request is intecepted by the UrlRoutungModule HTTP Module. WHen the UrlROutingModule interceps a reuqest , it wraps up the current HTTPContext in an HttpCOntextWrapper object. The HttpCOntextWrapper object derives from HttpContextBase class.
    -3. MVC handler executes
        - MVCHandler also inherit from the IHTTPAsyncHandler when ,MVC Handler executes it will call the BeginProcessRequest method of the httpAsyncHandler asynchronously.
        -When the process request methid is called a new controller gets created. The controller is created from a ControllerFactory. There is a ControllerBuilder Class which will set the ControleerFactory.
        -The RequetCOntext and the name of the Controller will be passed to the method CreateController Method to get the particular Controller.
    -4.Controller Executes
        controller is called and its action called requested by user
        -The Execute() method starts by creating the TempData object. TempData is a dictioanry derived from TempDataDictionary class and stroed in short lives session and it is a string key and object value
        -The Execute() method gets the Action from the RouteData based on the URL. The controller class then call the ControllerActionInvoker that builds a list of parameters from the request. 
        -These paramerets extracted from the request parameters, will act as method parameters. The parameters will be passed to whatever controller methods gets executed
        -Finally it will call the InvokeAction method to execute the Action
    -5.Render View Method Called
        -At last when we call return View() Render View method is called and puts response on the page to be displayed.
        -THe controller typycally either executer the RedirectToAction Method or the RenderView Method. When you call a controller's RenderView() method, the call is delegated to the current ViewEngine's RenderView() method. 
        -THe WebFormViewEngine.RenderView() method uses a class named the ViewLocator class to find the view. Next, it uses a BuildManager to create an instance of a ViewPage class from its path.

        Next, if the page has a master page, the location of the master page is set if the page has ViewData, the ViewData is set. Finally, the RenderVIew() method called on the ViewPage   



#### What is Razor View Engine?
    -Razor is a templating engine and markup syntax for embedding server-based code into webpages. The Razor syntax consists of Razor markup, C#, and html . ASP.NET MVC has imp,lemented a view engine which allows us to user Razor inside of an MVC application to produce HTML. Files containg Razor generally have a .cshtml file extension
#### What you mean by Routing in MVC?
    -ASP.NET MVC routing is a pattern matching system that is responsible for mapping incoming browser requests to specified MVC controller actions. For example, a URL http://domain/studentsinfo.aspx must match with the file studentsinfo.aspx that contains code and markup for rendering a response to the browser.
#### What is Layout in MVC?
    -An application may contain a specific UI portion that remains the same throughout the application, such as header, left navigation, right bar, or footer section. ASP.NET MVC introduced a Layout view which cotntains these common UI portions so that we dont have to write the same code in every page. E.G. an application UI may contain a header, left menu bar and footer section that remains the same on every page. Only the center changes dynamically.
#### What ConfigureServices() method does in Startup.cs?
    -ASP.NET Core includes a built-in dependency injection (DI) framework that makes configured services available throughout an app. e.g. logging component is a service. 
    The ConfigureServices method is a public method on your Startup class that takes IServiceCollection instance as a parameter and optionally returns an I ServiceProvider. The ConfigureServices method is called before Configure. This is important, because some features like ASP.NET MVC require certain services to be added in ConfigureServices before they can be wired up to the request pipeline.



    public void ConfigureServices(IServiceCollection services)
    {
        services.AddDbContext<RazorPagesMovieContext>(options =>
            options.UseSqlServer(Configuration.GetConnectionString("RazorPagesMovieContext")));

        services.AddControllersWithViews();
        services.AddRazorPages();
    }

    -Adding services to the services container makes them available within your application via dependency injection. Just as the Startup class is able to specify dependencies its methods require as parameters, rather than hard-coding to a specific implementation, so too can your middleware, MVC controllers and other classes in your application.
    -THe ConfigureServices method is also where you should add configuration option classes that you would like to have available in your app.

#### What Configure() method does in Startup.cs?
  
    
    -The Configure method is used to specify how the ASP.NET application will respond to individual Http requests. At it simpliest, you can configure every request to receive the same response. However, most real-world applications require more functionality than this. More complex sets of pipeline configuration can be encapsulated in middleware and added using extension methods on IApplicationBuilder.

    -Your configure method must accept an IApplicationBuilder parameter. Additional services, like IHostingEnvironment and ILoggerFactory may also be specified in which case these services will be injected by the server if they are available. In the following example from the default web site template, you can see several extension methods are used to configure the pipeline with support for BrowserLink, error pages, static files, ASP.NET MVC, and Identity:

    public void Configure(IApplicationBuilder app, IHostingEnvironment env, ILoggerFactory loggerFactory)
    {
    loggerFactory.AddConsole(Configuration.GetSection("Logging"));
    loggerFactory.AddDebug();

    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
        app.UseDatabaseErrorPage();
        app.UseBrowserLink();
    }
    else
    {
        app.UseExceptionHandler("/Home/Error");
    }

    app.UseStaticFiles();

    app.UseIdentity();

    // Add external authentication middleware below. To configure them please see http://go.microsoft.com/fwlink/?LinkID=532715

    app.UseMvc(routes =>
    {
        routes.MapRoute(
            name: "default",
            template: "{controller=Home}/{action=Index}/{id?}");
    });
    }

    Each Use extension method adds middleware to the request pipeline. E.G. the UseMvc extension method adds the routing middleware to the request pipeline and configures MVC as the default handler.


#### What is wwwroot folder in ASP.NET Core?
    -all the static files go in this folder. These are assets that te app will serve directly to clients, including HTML files, CSS files, image files and js files.
    -Code files should be placed outside of wwwroot, including c# files and razor views. Having wwwroot folder keeps a clean separation between code files and static files.
#### What’s the usage of [InternalsVisibleTo] attribute? What are pros and cons of it?  //not sure
    -It gives you the ability to expose methods marked internal to a specific assembly.
    -it breaks the rules of encapsulation
#### Explain what is WCF?
#### Mention what is the endpoint in WCF and what are the three major points in WCF?
#### Object Relational Mapping, Entity Framework
#### What is an ORM? What are benefits, when to use?
    ORM stands for Object Relational Mapper,it helps you take advantage of the oop principles while you are managing relational database. You are able to define what the structure in your database should look like, using code. Additionaly you can use code for your queries as well. An ORM library is a completely ordinary library written in your language of choice that encapsulates the code needed to manipulate data, so u aint use SQL anymore. 

    Benefits:
        -DRY: you wirte your data model in only one place, and its easier to update , maintain and reuse the code
        -it forces u to write mvc code, which makes it cleaner
        -a lot of stuff is done automatically like database handling
        -it lets you use OOP goodness like data inheritance without difficulties 
    
#### What is Entity Framework core? What are the advantages, limitations?
    -Entity Framework core is a modern object-database mapper for .NET . It supports LINQ queries, change tracking, updates, and schema migrations. EF Core works with many databases, including SQL Database, Postresql, MySQL etc..
    -EF core can serve as an object-relational mapper (O/RM) which:
        -enables .NET developers to work with databses using .NET objects.
        -Eliminates the need for most of the data-access code that typically needs to be written 

    -limitations: 
        -if there is any schema change in databse ef core will not work. You have to update schema in solution as well.

#### What is lazy loading?
    - Lazy loading is the process whereby an entity or collection of entities is automatically loaded from the database the first time that a property referring to the entity/entites. it also means delaying the loading of related data, until you specifically request for it. 

    -In the following example, the 'Author' entity contains the collection of Books. The Context first loads the author entity data from the databse, and then it will load the collection of books when we access the Books navigational property:
        using (var context = new BookStore())
        {
            var author = context.Authors
                .FirstOrDefault();
            
            var books = author.Books;
        }
    when the above code is executed, it will result in 2 SQL queries. in the first query, it will fetch the first author from the database: 
        SELECT TOP (1) 
            [c].[AuthorId] AS [AuthorId], 
            [c].[Name] AS [Name]
            FROM [dbo].[Authors] AS [c]
    when the navigational property Books in Author class is accessed, it will send the following query to fetch all the books related to that author.
    SELECT 
        [Extent1].[Id] AS [Id], 
        [Extent1].[Title] AS [Title], 
        [Extent1].[AuthorId] AS [AuthorId]
        FROM [dbo].[Books] AS [Extent1]
        WHERE [Extent1].[AuthorId] = @EntityKeyValue1

        -- EntityKeyValue1: '1' (Type = Int32, IsNullable = false)        

#### What is the difference between code first and DB first approach?
    - in Code first approach we will first create entity classes with properties defined in it. Entity framework will create the database and tables based on the entity classes defined. So database is generated from the code. When the .net code runs, database will get created.

    -The database first appriach created model codes (classes,properties, dbContext etc) from the database in the project and those classes become the link between the database and the controller.
    it also creates the entity framework from an existing database. We use all other functionalities, such as the model/database sync and the code generation
#### What is a migration script?
    -In real world projects, data models change as features get implemented: new entities or properties are added and removed, and database schemas needs to be changed accordingly to be kept in sync with the application. The migrations feature in EF Core provides a way to incrementally update the database schema to keep it in sync with the application/s data model while preserving existing data in the datbase
        - When a data model change is introduced, the developer uses EF Core tools to add a corresponding migration describing the updates necessary to keep the database schema in sync. EF core compares the current model against a snapshot of the old model to determine the differences, and generates migration source files; the files can be tracked in your projects source control like any other source file
        -Once a new migration has been generated it can be applied to database various ways. EF Core records all applied migrations in a special history table, allowing it to know which migrations have been applied and which aint.
#### What is a navigation property?
    -Navigation properties provide a way to navigate an association between two entity types. Every object can have a navigation property for every relationship in which it participates. Navigation properties allow you to navigate and manage relationshops in both directions, returning either a reference object or a collection.
#### Name 3 different attributes used in EF Core, what can they do for you?
    -from Data Annotations attributes in ef core can be applied on an entity class or properties to override default conventions.
        [Required] = can be applied to a property to specify that the corresponding column is a notnull column in the database
        [Key] can be applied to a property to specify a key property in an entity and make the corresponding column a PrmiaryKey Column in the database
        [MinLength] can be applied to a property to specify the minimum string length allowd in the corresponding column in the database. 